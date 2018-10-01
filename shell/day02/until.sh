#!/bin/bash
# until 语法演示

a=1

until [ "${a}" -eq 5 ]
do
    echo "${a}"
    a=$((a+1))
done
