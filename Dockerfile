FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Bring uv and uvx
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy only dependency metadata first (better caching)


COPY pyproject.toml poetry.lock ./

# Install deps with Poetry (no venv, only main deps)

RUN uvx --from=poetry poetry config virtualenvs.create false \
 && uvx --from=poetry poetry install --no-interaction --no-ansi --no-root

# Copy entrypoint
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh && sed -i 's/\r$//' entrypoint.sh

# Then copy source code (contains manage.py and core/)
COPY src/ .

EXPOSE 8000

CMD ["./entrypoint.sh"]