FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD [ "python", "main.py", "--host=0.0.0.0" ]
EXPOSE 5000