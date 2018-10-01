#!/bin/bash
# while语法演示
# 定义一个本地变量
a=1

while [ "${a}" -lt 5 ]
do
    echo "${a}"
    a=$((a+1))
done

