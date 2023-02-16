#FLAMES
name1=input("")
name1=list(name1)
name2=input("")
name2=list(name2)
for i in name1:
  for j in name2:
    if i==j:
      name1.pop(name1.index(i))
      name2.pop(name2.index(j))
    else:
      pass
length=len(name1)+len(name2)-name1.count(" ")-name2.count(" ")
L1=["Friends","Love","Affection","Marriage","Enemy","Siblings"]
while len(L1)>1:
  split_index = (length % len(L1) - 1)
  if split_index >= 0:
    right =L1[split_index + 1:]
    left = L1[: split_index]
    L1 = right + left
  else:
    L1 = L1[: len(L1) - 1]
print("relationship status:",L1[0])