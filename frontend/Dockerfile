FROM ubuntu:20.04
RUN apt-get install libproj-dev proj-data proj-bin
RUN apt-get install libgeos-dev
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD [ "python", "main.py"]
EXPOSE 5000