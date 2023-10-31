FROM python:3.11-slim-buster

RUN apt-get update && apt upgrade -y

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8350

ENV PYTHONUNBUFFERED=1

CMD ["python3", "main.py"]