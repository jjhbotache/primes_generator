# test2
list1 = [5,1,4,7,9,3,5,8]
list2 = [5,1,7]

print()
c=0
list1=set(list1)
list2=set(list2)
print(list1)
for x in list1:
    c+=1 
    print(f"time{c}  {x}")
    if x==1:
      list1 = [z for z in list1 if z != x ]
      print(list1)
print(list1)
 