FROM tiangolo/uwsgi-nginx-flask

COPY ./requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY ./db /app/db/

COPY ./data /app/data/

COPY ./schemas /app/schemas/

COPY ./services /app/services/

COPY ./resourse /app/resourse/

copy ./exceptions.py /app/exceptions.py

COPY app.py /app/main.py
CMD ["python","main.py"]

