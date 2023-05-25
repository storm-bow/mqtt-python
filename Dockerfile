FROM python:latest
WORKDIR /bow-chat
COPY requirements.txt .
COPY bow-chat.py .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "bow-chat.py"]