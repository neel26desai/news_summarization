FROM python:3.10-slim

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY server.py ./server.py

ENV FLASK_APP=server.py

CMD ["flask", "run", "--host=0.0.0.0", "-p", "80"]