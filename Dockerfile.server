FROM python:3.10-slim

WORKDIR /app

COPY mysocketserver.py /app/

RUN pip install Pyro4

EXPOSE 5000

CMD ["python", "mysocketserver.py"]