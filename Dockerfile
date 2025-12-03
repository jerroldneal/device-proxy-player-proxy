FROM audio-driver-proxy:latest

# Install audio dependencies (mpg123 for playing files if needed)
RUN apt-get update && apt-get install -y \
    mpg123 \
    && rm -rf /var/lib/apt/lists/*

# Copy the application
COPY main.py /app/main.py

# Run the application directly
CMD ["python", "-u", "/app/main.py"]
