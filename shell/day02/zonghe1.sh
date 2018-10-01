#!/bin/bash
# 脚本综合演练


a="$1"
# 编写脚本帮助信息
usage(){
    echo "脚本$0使用方式$0[ start|stop|restart ]"
}


# 脚本主框架
if [ "$#" -eq 1 ]
then 
    case "${a}" in
        start)
            echo "服务启动中..."
            ;;
        stop)
            echo "服务关闭中..."
            ;;
        restart)
            echo "服务重启中..."
            ;;
        *)
            usage
            ;;
    esac
else
    usage
fi



