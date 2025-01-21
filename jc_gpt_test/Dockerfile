FROM python:3.12.4
WORKDIR /jc_gpt_test_app
RUN pip install gunicorn==20.1.0
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . .
RUN python manage.py collectstatic --noinput
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "jc_gpt_test.wsgi"] 
