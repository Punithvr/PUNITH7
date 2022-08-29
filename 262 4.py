print("enter the marks obtained in 3 subjects")
markOne=int(input())
markTwo=int(input())
markThree=int(input())
total=markOne+markTwo+markThree
avg=total/3
if avg>=81 and avg<=100:
    print("A")
elif avg>=51 and avg<81:
    print ("B")
elif avg>=0 and avg<51:
    print("c")
