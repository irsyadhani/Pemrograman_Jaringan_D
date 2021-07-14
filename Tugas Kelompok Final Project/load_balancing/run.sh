# NOTE
# gak dipakek soalnya while true di python thread
# jadi gabisa di daemon

#!/bin/bash

thread () {
    if [[ $1 -eq 0 ]]
    then
        echo "kill thread"
        pkill -f server_thread_http.py
        exit 0
    fi

    port=9000
    for (( i=9000; i<$(($port+$1)); i++ ));
    do
        python3 server_thread_http.py -p $i
        echo "Server port $i berjalan"
    done
    exit 0
}

async () {
    if $2 == 0
    then
        pkill -f async_server.py
        exit 0
    fi

    for (( i=9100; i<$2; i++ ))
    do
        python3 async_server.py $i
    done
}

if [ "$1" = "-t" ]
then
    thread $2
elif [ "$1" = "-a" ]
then
    async $2
    exit 0
fi


# python3 async_server.py 9002 &
# python3 async_server.py 9003 &
# python3 async_server.py 9004 &
# python3 async_server.py 9005 &