FROM python:3.7.1

# copy requirements.txt and pip install to utilize docker caching mechnism so
# we won't install all the packages over again whenever we modified the codes
COPY requirements.txt /euchre_game/

WORKDIR /euchre_game

RUN pip install -r requirements.txt

ENV FLASK_APP app/__init__.py
ENV FLASK_DEBUG 1

RUN echo "alias flask='python -m flask'\n\ 
PS1='🐳  \[\033[1;36m\]\h \[\033[1;34m\]\W\[\033[0;35m\] \[\033[1;36m\]# \[\033[0m\]'\n\
LS_OPTIONS='--color=auto'\n" \
>> ~/.bashrc

CMD ["python", "-u", "-m", "flask", "run", "-h", "0.0.0.0", "-p", "5000"]
