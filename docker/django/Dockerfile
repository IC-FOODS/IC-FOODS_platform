FROM python:3.9.6-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add postgresql-dev gcc python3-dev musl-dev libffi-dev jpeg-dev zlib-dev

WORKDIR /usr/src/

RUN python3 -m pip install --upgrade pipenv
# install dependencies
COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --system --deploy

# copy project
COPY . .

WORKDIR /usr/src/burulka

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
