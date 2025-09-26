# reverse number triangle pattern
rows=5
while rows>=1:
    columns=1
    while columns<=rows:
        print(columns,end=" ")
        columns+=1
    print()
    rows-=1