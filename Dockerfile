FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
ENV SERVICE_PORT 8080
ENV PKG_DIR /tmp/pkg
ENV SRC_DIR /tmp/src

COPY pkg/*.txt ${PKG_DIR}/
RUN pip install --upgrade pip && \
    pip install --upgrade -r ${PKG_DIR}/pip_requirements.txt

COPY src ${SRC_DIR}
WORKDIR ${SRC_DIR}

EXPOSE ${SERVICE_PORT}

CMD ["python3", "atable.py", "-app", "wine_info_app"]
