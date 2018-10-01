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
        gevent.spawn(downloader, "1.jpg", "http://img.netbian.com/file/2018/0315/110ea9f997974cf8da211b2c9be4db96.jpg"),
        gevent.spawn(downloader, "2.jpg", "http://img1.mm131.me/pic/3454/0.jpg")])
if __name__ == "__main__":
    main()
