# Use a Python base image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml uv.lock README.md ./
COPY calculator_mcp/ ./calculator_mcp/

# Install dependencies using uv
RUN pip install uv && uv sync

# Expose the port (will be set by PORT environment variable)
EXPOSE 8080

# Set environment variable for Python
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["uv", "run", "calculator-mcp"]