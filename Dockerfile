# Step 1: Use the official Python image as a base image
FROM python:3.12.3

# Step 2: Set environment variables to avoid prompts during installation
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Step 5: Set the working directory in the container
WORKDIR /app

COPY . /app/

EXPOSE 8051

RUN apt-get update
RUN apt-get install -y locales

RUN sed -i -e 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen
RUN dpkg-reconfigure --frontend=noninteractive locales

RUN LANG=pt_BR.UTF-8
RUN LC_AL=pt_BR.UTF-8

RUN mkdir media

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD [ "sh", "./entrypoint.sh" ]
