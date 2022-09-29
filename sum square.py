def sumsquare(l):
    int(inpit(1))
    odd=0
    even=0
    for i in l:
        if i%2==0:
            even = even + i**2
            odd = odd + i**2
            l=[odd,even]
            return(l)
        print("enter the sumsquare",(1))
        print(sumsquare(l))
