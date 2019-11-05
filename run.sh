#!/usr/bin/env bash

function start () {
    pipenv run gunicorn -b 0.0.0.0:5555 --reload app:api
}

function stop () {
    ps -ef | grep gunicorn | awk '{print $2}' | xargs kill -9
}


env="$SCRIPT_HOME/.env"
if [[ -f $env ]]; then source $env; fi

case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    *)
    echo "Usage: run.sh {start|stop}"
    exit 1
esac
