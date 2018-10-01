#!/bin/bash
# 多f语句的使用场景

if [ "$1" == "start" ]
then 
    echo "1"
elif [ "$1" == "stop" ]
then
    echo "2"
elif [ "$1" == "restart" ]
then
    echo "3"
else
    echo "4"
fi
