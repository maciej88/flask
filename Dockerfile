ROM python:3.8-slim-buster

WORKDIR /usr/src/app

RUN python -m venv venv
RUN . venv/bin/activate
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /usr/src/app
EXPOSE 5000
CMD [ "python", "-u", "guess_game.py" ]
