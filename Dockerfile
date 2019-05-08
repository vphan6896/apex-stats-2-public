FROM ubuntu:16.04
RUN apt-get update -y \ 
    && apt-get upgrade
COPY . /app
WORKDIR /app
RUN apt install python-pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app/app.py"]
