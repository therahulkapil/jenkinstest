FROM python:3.9
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
COPY . .
CMD [ "python","app.py" ]