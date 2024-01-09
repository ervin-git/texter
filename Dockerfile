# build image
FROM python:3.11 as builder

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH="$PYTHONPATH:/code/texter" \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    # poetry
    POETRY_VERSION=1.6.1

RUN pip install poetry==${POETRY_VERSION} \
    && poetry config virtualenvs.in-project true

WORKDIR /code

COPY ./pyproject.toml ./poetry.lock ./
RUN poetry install --compile --no-interaction --no-ansi --no-root -vvv $(test "$(echo $ENV | awk '{print tolower($0)}')" != "dev" && echo "--only main")

# runtime image
FROM python:3.11 as runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH="$PYTHONPATH:/code/texter" \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    # virtual envs
    VIRTUAL_ENV=/code/.venv \
    PATH="/code/.venv/bin:$PATH" \
    # tz
    TZ=America/Chicago

RUN apt-get update && \
    apt-get install -yq --no-install-recommends tini && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /code

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}
COPY ./texter/ ./texter/

ENTRYPOINT ["tini", "--"]
CMD ["uvicorn", "texter.texter:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
