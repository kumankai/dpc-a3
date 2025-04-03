FROM python:3.10-slim

WORKDIR /app
COPY pyroserver.py .

RUN pip install Pyro4

CMD ["python", "pyroserver.py"]