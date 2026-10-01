FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY servir.py .
COPY modelos ./modelos
CMD ["sh", "-c", "uvicorn servir:app --host 0.0.0.0 --port ${PORT:-8000}"]