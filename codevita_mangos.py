num_bags=input()

mangos_in_bags=input()
mangos_list=mangos_in_bags.split()
lst=[]
for elements in mangos_list:
    element=int(elements)
    lst.append(element)
lst.sort()

total=0
for element in lst:
    total=total+element

if (total%3)==0:
    print(total)

else:
    for element in lst:
        total=total-element
        if (total%3)==0:
            print(total)
            break
        else:
            continue
    
