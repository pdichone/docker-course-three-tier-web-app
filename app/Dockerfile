FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 80 
# 5002

CMD ["python", "app.py"]
