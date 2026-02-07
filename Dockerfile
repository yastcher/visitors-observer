FROM python:3.11-slim AS builder

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential gcc cmake curl && \
    rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-editable

COPY . .

HEALTHCHECK --interval=1m --timeout=30s \
  CMD curl -f http://localhost:5555/status || exit 1

EXPOSE 5555
CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5555"]
