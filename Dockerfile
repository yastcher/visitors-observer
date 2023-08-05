FROM python:3.11-slim as builder
RUN apt update && apt install --no-install-recommends -y build-essential gcc cmake curl
WORKDIR /app
COPY ./requirements*.txt /app/
RUN pip install --upgrade pip
RUN --mount=type=cache,target=/root/.cache \
    pip wheel --wheel-dir /wheels -r requirements.txt
RUN --mount=type=cache,target=/root/.cache \
    pip wheel --wheel-dir /wheels --no-deps -r requirements-torch.txt
RUN --mount=type=cache,target=/root/.cache \
    pip wheel --wheel-dir /wheels --no-deps -r requirements-compile.txt

# FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04 as runtime
# RUN apt-key del 7fa2af80 && \
#     apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub && \
#     apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu2004/x86_64/7fa2af80.pub
# RUN apt update && \
#     apt install software-properties-common -y && add-apt-repository ppa:deadsnakes/ppa && \
#     DEBIAN_FRONTEND=noninteractive apt -qq  install --no-install-recommends -y curl python3.11 python3-pip libglu1-mesa libglib2.0-0 libc6 \
#     && apt clean && rm -rf /var/lib/apt/lists/*
# COPY --from=builder /wheels /wheels
# RUN pip install --upgrade pip

RUN pip install --no-cache /wheels/* && rm -rf /wheels

WORKDIR /app
COPY . .

HEALTHCHECK --interval=1m --timeout=30s \
  CMD curl -f http://localhost:5555/status || exit 1

EXPOSE 5555
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5555"]
