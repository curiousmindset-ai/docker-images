# syntax=docker/dockerfile:1

############################
# Builder stage
############################
FROM python:3.12-slim AS builder

WORKDIR /build

# System deps needed for building wheels (kept in builder only)
RUN apt-get update \
 && apt-get install -y --no-install-recommends gcc \
 && rm -rf /var/lib/apt/lists/*

# Create a virtual environment to copy into runtime image
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies first for better layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

############################
# Runtime stage
############################
FROM python:3.12-slim

# Create a non-root user
RUN useradd --create-home --shell /usr/sbin/nologin appuser

# Copy the virtual env from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app

# Copy application code
COPY app.py /app/app.py

# Reduce Python noise + improve container behavior
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

EXPOSE 8080

# Simple healthcheck endpoint
HEALTHCHECK --interval=10s --timeout=3s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/healthz').read()" || exit 1

# Drop privileges
USER appuser

# Run app
CMD ["python", "app.py"]
