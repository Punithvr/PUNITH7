list_1 = input().split() 
dict_1={} 
for ele in list_1: 
    if ele in dict_1: 
        dict_1[ele] += 1 
    else: 
        dict_1[ele] = 1 
for key,value in dict_1.items(): 
    print(key,"-",value)
