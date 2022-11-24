FROM python:3.10.8
RUN pip install --upgrade pip
RUN mkdir /app1
WORKDIR /app1
COPY . /app1
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT python
CMD ./app.py