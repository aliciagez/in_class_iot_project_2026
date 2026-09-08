FROM python:3.13-slim

WORKDIR /app
COPY comsumer.py /app/
COPY utils /app/utils
COPY pyproject.toml /app/

RUN pip install --no-cache-dir uv
RUN uv sync --no-dev

#PYTHONUNBUFFERD=1, kan ha detta istället för flush

CMD [ "uv", "run", "comsumer.py"]
