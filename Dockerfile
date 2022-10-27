FROM python:3.12.0a1-slim-bullseye
ADD rest-example.py /
RUN pip install flask
RUN pip install flask_restful
EXPOSE 8080
CMD [ "python", "./rest-example.py"]
