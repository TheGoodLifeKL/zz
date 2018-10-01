def create_num(all_num):
    a, b = 0, 1
    i = 1
    while i < all_num:
        #print(a)
        yield a
        a, b = b, a+b
        i += 1
obj = create_num(20)
for i in obj:
    print(i)
