# put your python code here
user = input()
l = [i for i in user]
l2 = []

if len(l) >= 6:
    l2.append(l[0])
    l.remove(l[0])
    l.reverse()
    
    print("".join(l2) + "".join(l))
  
else:
    l.reverse()
    t = "".join(l)
    print(int(t))

 