FROM python:3.11.5

RUN apt-get update -y
RUN apt-get install build-essential -y

WORKDIR /app-docker
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .

# Expose port 5001 for the Flask app
EXPOSE 5001

# Use gunicorn to run the Flask app on port 5001
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "app:app"]
