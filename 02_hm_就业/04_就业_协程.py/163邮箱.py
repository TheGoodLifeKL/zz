import re
def main():
    email_addr = input("请输入你的网易邮箱:")
    ret = re.match(r"[a-zA-Z0-9]{4,20}@163\.com$", email_addr)
    if ret:
        print("%s符合要求"%email_addr)
    else:
        print("%s不符合要求"%email_addr)
if __name__ == "__main__":
    main()
