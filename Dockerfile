FROM python:3.9-slim
WORKDIR /app
COPY ./ /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 8000
ENV HOSTNAME 51.250.98.133
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]