FROM python:3.12.4
WORKDIR /jc_gpt_test_app
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . .
CMD ["python", "manage.py", "runserver", "0:8000"] 
