FROM python:3.9-slim  

ENV PYTHONDONTWRITEBYTECODE=1 \  
    PYTHONUNBUFFERED=1  

RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY src/requirements.txt .

RUN uv pip install -r requirements.txt --system 

COPY src/ .

EXPOSE 8000

CMD ["./entrypoint.sh"]