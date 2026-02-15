# args is used for accepting multiple arguments 

def add(*args):
    total = 0
    for num in args:
        total += num
    print("Total:", total)

add(10, 20)
add(10, 20, 30)
add(5, 15, 25, 35)
