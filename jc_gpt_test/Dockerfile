# FROM python:3.12-slim
# WORKDIR /jc_gpt_test_app
# RUN apt-get update && apt-get install -y iputils-ping
# RUN pip install gunicorn==20.1.0
# COPY requirements.txt .
# RUN pip install -r requirements.txt --no-cache-dir
# COPY . .
# RUN python manage.py collectstatic --noinput
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "jc_gpt_test.wsgi"] 


FROM python:3.12-slim
WORKDIR /jc_gpt_test_app

RUN apt-get update && apt-get install -y iputils-ping
RUN pip install gunicorn==20.1.0

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

# Создаем директорию для статики
RUN mkdir -p /var/www/jc_gpt_test/static

# Запускаем collectstatic
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "jc_gpt_test.wsgi"]