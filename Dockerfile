FROM python:3.9-slim

WORKDIR /app

COPY main.py /app/

RUN chmod +x /app/main.py

ENTRYPOINT ["python", "main.py"]

