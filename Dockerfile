FROM python:3.9-slim
LABEL authors="gregglegarda"

#set envionment variables
ENV PYTHONUNBUFFERED 1

WORKDIR /

RUN apt update
RUN apt install python3 -y

# Install core dependencies.
RUN apt-get update && apt-get install -y libpq-dev build-essential


COPY requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt


COPY assets/ /assets/
COPY redis_code/ /redis_code/
COPY redis_code/ccmd_data/ /redis_code/ccmd_data/
COPY joint_data/ /joint_data/

COPY page_data_model/ /page_data_model/
COPY page_historical_data/ /page_historical_data/
COPY page_home/ /page_home/
COPY page_incident_form/ /page_incident_form/
COPY page_interactive_map/ /page_interactive_map/

COPY pages/ /pages/

COPY app.py ./app.py
COPY app_theme.py ./app_theme.py
COPY data_connection.py ./data_connection.py
COPY functions.py ./functions.py



CMD [ "python", "app.py"]
#CMD gunicorn -b :$8080 main:app
#ENTRYPOINT

#Expose server port
EXPOSE 8050
EXPOSE 6379