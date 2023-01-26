FROM python:alpine3.17
WORKDIR /app
COPY requirement.txt .
RUN pip install -r requirement.txt
COPY app.py .
COPY templates templates
COPY static static
ENTRYPOINT [ "./app.py" ]
