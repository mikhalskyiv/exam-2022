FROM ubuntu:18.04
RUN apt update -y && apt install python3 -y
WORKDIR /app
COPY . /app
CMD python3 app.py
