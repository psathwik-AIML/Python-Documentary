# right angle triangle pattern
rows=1
while rows<=5:
    space=1
    while space<=5-rows:
        print(" ",end=" ")
        space+=1
    star=1
    while star<=rows:
        print("*",end=" ")
        star+=1
    print()
    rows+=1