FROM ubuntu:20.04
RUN sudo apt-get install libproj-dev proj-data proj-bin
RUN sudo apt-get install libgeos-dev
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD [ "python", "main.py"]
EXPOSE 5000