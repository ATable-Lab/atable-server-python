FROM python:3.8

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

WORKDIR backend

CMD ["python3", "server.py"]
