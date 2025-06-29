# Dockerfile

# 1. Use an official lightweight Python runtime as a parent image
FROM python:3.11-slim

# 2. Set the working directory in the container
WORKDIR /app

# 3. Copy the dependency definition files
COPY pyproject.toml uv.lock* ./

# 4. Install uv, the package installer specified in your project
RUN pip install uv

# 5. Install project dependencies
RUN uv pip install --system -r pyproject.toml

# 6. Copy the rest of your application's code into the container
COPY . .

# 7. The command to run your application when the container starts.
#    It will use the PORT environment variable set by Smithery.
CMD ["python", "main.py"]