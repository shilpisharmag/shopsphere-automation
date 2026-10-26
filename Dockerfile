FROM python:3.12-slim
WORKDIR /app
COPY api/requirements.txt /app/api/requirements.txt

RUN pip install --no-cache-dir --retries 5 --timeout 60 -r /app/api/requirements.txt

COPY api/ /app/api/
COPY ui/ /app/ui/

EXPOSE 5000
ENV FLASK_HOST=0.0.0.0

CMD ["python","api/app.py"]
