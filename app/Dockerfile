FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEPLOY_ENV=1

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-root





CMD python manage.py collectstatic --noinput \
    && python manage.py makemigrations --noinput \
    && python manage.py migrate --noinput \
    && gunicorn settings.wsgi:application --bind 0.0.0.0:8000
