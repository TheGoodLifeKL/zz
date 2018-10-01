from threading import *
i = 0 
def work1(num):
    global i
    for s in range(num):
        i += 1
    print("%d" %i)
def work2(num):
    global i
    for s in range(num):
        i += 1
    print("%d" %i)
    
def main():
    t1 = Thread(target=work1, args=(1000000,)) 
    t1.start()
    t2 = Thread(target=work2, args=(1000000,)) 
    t2.start()
if __name__ == "__main__":
    main()
