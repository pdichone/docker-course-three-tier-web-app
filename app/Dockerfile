FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5002 

# 5002 this is for local dev

CMD ["python", "app.py"]
