FROM python:3.11.3

WORKDIR /app

# Install dependencies first 
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["python", "run.py"]