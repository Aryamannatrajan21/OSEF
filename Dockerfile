# OSEF Production Engine OCI Container
# Builds an immutable, zero-dependency environment for running EKG analysis, EPE policy evaluation, and MCP server.

FROM python:3.12-slim

# Prevent Python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /workspace

# Install system dependencies required for repository graph analysis
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy project configuration and source modules
COPY pyproject.toml README.md ./
COPY src/ ./src/
COPY reference-plugins/ ./reference-plugins/

# Install OSEF CLI and engine dependencies
RUN pip install --no-cache-dir .

# Set entry point to the OSEF command-line interface
ENTRYPOINT ["osef"]
CMD ["--help"]
