FROM python:latest

WORKDIR /usr/src/super-pancake

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:super-pancake", "--host", "0.0.0.0", "--port", "8000"]
