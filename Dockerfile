FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
# Gunicorn is a production-grade server needed for cloud deployment
CMD ["gunicorn", "app:app"]
