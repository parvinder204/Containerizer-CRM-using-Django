FROM python

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y libpq-dev

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY . .

EXPOSE 8000

RUN python manage.py migrate

CMD ["python","manage.py","runserver","0.0.0.0:8000"]