FROM python:alpine3.17
WORKDIR /app
COPY requirement.txt .
RUN pip install -r requirement.txt
COPY app.py .
COPY templates templates
#COPY static static  #serving staticfiles from nginx server
ENTRYPOINT [ "./app.py" ]