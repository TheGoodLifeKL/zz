import threading 
import time
def saySorry():
    print("对不起，我错了...")
    time.sleep(5)
def main():
    for i in range(10):
        t = threading.Thread(target=saySorry)
        t.start()
if __name__ == "__main__":
    main()
