FROM python:3.7-alpine

WORKDIR /app
COPY . .
RUN pip install -Ur requirements.txt && mkdir reports
WORKDIR /app/scripts

ENTRYPOINT ["python3", "regression_scan.py"]
