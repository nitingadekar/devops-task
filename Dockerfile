FROM python:latest

#COPY requirements.txt .

# install dependencies
#RUN pip install -r requirements.txt
RUN python -m pip install flask datetime pytz
# copy the content of the local src directory to the working directory
COPY rest.py .

# command to run on container start
EXPOSE 8080
CMD [ "python", "./rest.py" ]
