FROM python:3.10-slim AS build-stage
WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir flet flet-web

FROM python:3.10-slim
EXPOSE 8550
ENV FLET_SERVER_PORT=8550
ENV FLET_FORCE_WEB_SERVER=true

ENV PYTHONPATH=/usr/local/lib/python3.10/site-packages
WORKDIR /app

COPY --from=build-stage /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=build-stage /usr/local/bin /usr/local/bin
COPY converter.py .

RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

CMD ["python", "converter.py"]