FROM python:3.11.3
WORKDIR /
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD [ "python", "main.py"]
EXPOSE 5000