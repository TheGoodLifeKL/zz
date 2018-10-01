import urllib.request
import gevent
from gevent import monkey
monkey.patch_all()

def downloader(file_name,url):
    reponse = urllib.request.urlopen(url)
    photo_data = reponse.read()
    with open(file_name, "wb") as f:
        f.write(photo_data)
def main():
    gevent.joinall([
        gevent.spawn(downloader, "1.jpg", "http://imgsrc.baidu.com/image/c0%3Dshijue1%2C0%2C0%2C294%2C40/sign=739b937b8f35e5dd8421ad9c1eafcd9a/e61190ef76c6a7eff242db0ff7faaf51f3de66b6.jpg"),
        gevent.spawn(downloader, "2.jpg", "http://pic1.win4000.com/wallpaper/b/59c9adad14908.jpg")
    ])
if __name__ == "__main__":
    main()
