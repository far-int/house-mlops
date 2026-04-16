FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --default-timeout=1000 -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]