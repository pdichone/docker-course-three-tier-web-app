FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 80  
# 80 is expected for beanstalk
# 5002 this is for local dev

CMD ["python", "app.py"]
