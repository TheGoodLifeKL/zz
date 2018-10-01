import re
import urllib.request
import gevent
from gevent import monkey
monkey.patch_all()

def downloader(url,file_name):
    reponse = urllib.request.urlopen(url)
    img_url = reponse.read()
    with open(file_name, "wb") as f:
        f.write(img_url)
def main():
    f = open("1.html")
    content = f.read()
    ret = re.findall(r"https://.*?\.jpg", content)
    img_url_list = list() # 创建列表用来储存gevent
    i = 0
    for s in ret:
        i += 1
        img_url_list.append(gevent.spawn(downloader,  s, str(i) + ".jpg"))
    gevent.joinall(img_url_list)

if __name__ == "__main__":
    main()
