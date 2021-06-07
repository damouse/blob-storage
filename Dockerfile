FROM python:3.9

ENV HOME=/app
WORKDIR /app

COPY stocks /app/stocks
COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

CMD /usr/local/bin/python3 stocks/main.py