FROM python:3.11-slim

WORKDIR /api

# install required packages for system --> MUST RUN THIS FOR THIS TO WORK!
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY . /api


RUN pip install mysqlclient

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

CMD ["python", "api.py"]
