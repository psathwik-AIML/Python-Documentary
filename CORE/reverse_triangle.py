# Reverse Triangle pattern code 
rows=5
while rows>=1:
    space=1
    while space<=5-rows:
        print(" ",end=" ")
        space+=1
    star=1
    while star<=2*rows-1:
        print("*",end=" ")
        star+=1
    print()
    rows-=1