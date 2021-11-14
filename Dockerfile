FROM python:3.8

RUN mkdir app

COPY . app/

WORKDIR /app/

RUN pip install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8080", "--server.address=0.0.0.0"]