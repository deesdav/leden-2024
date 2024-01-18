print("LIFO")
li = [1, 2, 3, 4]

while len(li) > 0:
    print(li.pop())

print("FIFO")
li = [1, 2, 3, 4]
while len(li) > 0:
    print(li[0])
    del li[0]
