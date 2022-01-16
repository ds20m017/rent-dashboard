FROM python:3.8
COPY . /app
WORKDIR /app
RUN apt-get update && apt-get install -y git
RUN apt-get install -y libproj-dev proj-data proj-bin  
RUN apt-get install -y libgeos-dev
RUN apt-get install -y python3-dev
RUN pip install -r requirements.txt
CMD [ "python", "main.py"]
EXPOSE 5000