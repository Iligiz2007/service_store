FROM python:3.11-slim


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /usr/src/app

RUN pip install --upgrade pip 
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "project.asgi:application"]

