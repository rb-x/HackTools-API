FROM python:3.10-slim as base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1


# Stage 1: Install pipenv and compilation dependencies
FROM base AS python-deps


RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy


# Stage 2: Run the application in a virtualenv
FROM base AS runtime

# Copy virtual env from python-deps stage
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"


RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser


COPY app /home/appuser/app
COPY run.py /home/appuser/run.py


EXPOSE 8000


ENV VIRTUAL_ENV /.venv


CMD ["python3", "run.py"]
