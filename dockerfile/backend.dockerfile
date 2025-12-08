FROM python:3.11-slim
WORKDIR /kinopark-backend
COPY ./requirements /kinopark-backend/requirements

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir .

COPY . /kinopark-backend

EXPOSE 8000

CMD ["bash","-c","python manage.py make_migrations && python manage.py migrate && python manage.py collectstatic --noinput && gunicorn kinopark_backend.wsgi:application --bind 0.0.0:8000"]

