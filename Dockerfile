FROM python:3.11

WORKDIR /app

RUN pip install pipenv

COPY Pipfile Pipfile.lock ./

RUN pipenv install --deploy --ignore-pipfile

COPY . . 

EXPOSE 8080

CMD ["pipenv","run","python","main.py"]