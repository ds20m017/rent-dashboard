FROM python:3.8
COPY . /app
WORKDIR /app
RUN apt-get install libproj-dev proj-bin proj-data
RUN apt-get install libgeos-dev
RUN pip install -r requirements.txt
CMD [ "python", "main.py"]
EXPOSE 5000