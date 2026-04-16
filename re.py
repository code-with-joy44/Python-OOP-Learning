import area


def sum():
    sum=0
    for x in range(1,100,2):
        sum=sum+x
    print(sum)
add=sum()

from area import tri
area.tri(10,10)
