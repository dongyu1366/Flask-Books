FROM python:3.8

# set a directory for the app
WORKDIR /app

# Bundle app source
COPY ./src .

# install dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# define the port number the container should expose
EXPOSE 5000

# run the command

CMD ["python", "application.py"]
