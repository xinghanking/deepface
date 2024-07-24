#!/bin/bash

HOST="127.0.0.1"
PORT=8000
WORKERS=1

BASE_ROOT=$(dirname $(dirname "$(readlink -f "$0")"))
LOG_PATH="$BASE_ROOT/logrun.log"
APP_NAME="main"
VENV_PATH="$BASE_ROOT/.venv"
source "$VENV_PATH/bin/activate"
cd "$BASE_ROOT"

start() {
    echo "Starting Uvicorn server..."
    nohup uvicorn $APP_NAME:app --workers $WORKERS --host "$HOST" --port $PORT > $LOG_PATH 2>&1 &
}

reload() {
    echo "Reloading Uvicorn server..."
    PID=$(lsof -t -i :$PORT)
    kill -HUP "$PID"
}

stop() {
    echo "Stopping Uvicorn server..."
    PID=$(lsof -t -i :$PORT)
    kill -TERM uvicorn
}

case "$1" in
    start)
        start
        ;;
    reload)
        reload
        ;;
    stop)
        stop
        ;;
    restart)
        stop
        start
        ;;
    *)
        echo "Usage: $0 {start|reload|stop}"
        exit 1
esac