# euchre_game

## Requirements

This app requires the newest version of docker and docker-compose installed as of the writing of this README, October 31, 2018.

## Installation

```shell
docker-compose build
```

## Execution / Run

```shell
docker-compose up
```

The app will be then available in your browser @ `http://localhost:5000`

# SSH Into Container

add this to your `~/.bashrc`:
```shell
alias docker-bash="docker-compose exec -u 1000:1000 euchre-game bash"
```

and run
```shell
docker-bash
```
to ssh into the container
