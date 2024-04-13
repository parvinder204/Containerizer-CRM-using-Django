FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY . /code
COPY requirements.txt /code/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]