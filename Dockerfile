FROM python:3.7-alpine

WORKDIR /code

# Install any needed packages specified in requirements.txt
RUN apk update && \
    apk add --no-cache make gcc g++ libgcc libstdc++ libsodium musl libzmq zeromq-dev linux-headers python3-dev && \
    pip install --upgrade pip && \
    pip install requests selenium && \
    rm -Rf /tmp/* && \
    rm -Rf /root/.cache/*

CMD ["python3", "/code/test.py"]
