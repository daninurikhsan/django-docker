FROM python:3.9

# ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBEFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /code/

# EXPOSE 8009

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8009" , "--noreload"]
