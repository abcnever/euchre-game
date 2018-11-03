FROM python:3.7.1

# copy requirements.txt and pip install to utilize docker caching mechnism so
# we won't install all the packages over again whenever we modified the codes
COPY requirements.txt /euchre_game/

WORKDIR /euchre_game

RUN pip install -r requirements.txt

ENV FLASK_APP app/__init__.py
ENV FLASK_DEBUG 1

RUN echo 'alias flask="python -m flask"' >> ~/.bashrc

CMD ["python", "-u", "-m", "flask", "run", "-h", "0.0.0.0", "-p", "5000"]
