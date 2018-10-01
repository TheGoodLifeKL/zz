def line(k,b):
    def create_y(x):
        print(k*x + b)
    return create_y
s = line(2,2)
s(0)
s(1)
s(2)

