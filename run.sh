#!/usr/bin/env bash

env="$SCRIPT_HOME/.env"
if [[ -f $env ]]; then source $env; fi

if [[ -z $API_PORT ]]; then API_PORT=5555; fi


function start () {
    pipenv run gunicorn -b 0.0.0.0:$API_PORT --reload app:api
}

function stop () {
    ps -ef | grep gunicorn | awk '{print $2}' | xargs kill -9
}

case "$1" in
    start)
        start
        cat << EOF >/dev/null # sample_run_afterward="
            curl -X POST localhost:$API_PORT/login -d '{ "username": "doan", "password": "doan"}' -H 'Content-Type: application/json'

            token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE1NzMwMTg1OTV9.jG0z4vul4IQAYpPuBvgMi6xbbGq6r9-O8BafL8fysAo  # get token from /login above
                curl -X GET localhost:$API_PORT/customer    -H 'Content-Type: application/json' -H "Authorization: Bearer $token"
                curl -X GET localhost:$API_PORT/customer/1  -H 'Content-Type: application/json' -H "Authorization: Bearer $token"

                curl -X POST localhost:$API_PORT/customer  -H 'Content-Type: application/json' -H "Authorization: Bearer $token"  -d '{ "name": "SOME NEW NAME", "dob": "1999-11-22"}'

                curl -X PUT localhost:$API_PORT/customer/1  -H 'Content-Type: application/json' -H "Authorization: Bearer $token"  -d '{ "name": "SOME UPDATED NAME"}'
                curl -X PUT localhost:$API_PORT/customer/1  -H 'Content-Type: application/json' -H "Authorization: Bearer $token"  -d '{ "dob": "1999-11-23"}'

                curl -X DELETE localhost:$API_PORT/customer/1  -H 'Content-Type: application/json' -H "Authorization: Bearer $token"
        "
EOF
        ;;
    stop)
        stop
        ;;
    *)
    echo "Usage: run.sh {start|stop}"
    exit 1
esac
