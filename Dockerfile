FROM python:3.12.5-bookworm
WORKDIR /app
COPY . /app/
EXPOSE 80
RUN pip install -r requirements.txt
RUN python3 -m pytest
CMD ["python", "app.py"]

