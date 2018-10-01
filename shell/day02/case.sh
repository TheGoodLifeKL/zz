#!/bin/bash
case "$1" in 
    "start")
        echo "服务启动中..."
        ;;
    "stop")
        echo "服务关闭中..."
        ;;
    "restart")
        echo "服务重启中..."
        ;;
    *)
        echo "$0 脚本的使用方式: $0 [ start|stop|restart ]"
        ;;
esac
