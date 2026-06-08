FROM python:3.10-slim
EXPOSE 8550
ENV FLET_SERVER_PORT=8550
ENV FLET_FORCE_WEB_SERVER=true
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install flet
CMD ["python", "converter.py"]