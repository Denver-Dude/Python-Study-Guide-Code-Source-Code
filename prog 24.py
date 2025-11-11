lst = list(range(1,11))
print(lst)

tmp=[12,13,14,15]
print(lst+tmp)#if simply add
lst.extend(tmp)#if modify and add
print(lst)

x = lst.pop()
print(x)
print(lst)#to remove element from the end

lst.insert(0,x)#this will insert the last element in the first place


y =lst.pop(0)#will pop the element in first of the list
lst.append(y)
print(lst)
#element taken and kept back
