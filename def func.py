a = [123, 456, 789]
b = [str(item) for item in a]
s = b[0] + b[1] + b[2]
s = list(s)
k=[]
for i in s:
	k.append(i)
v =[int(item) for item in k]
v = sum(v)
print(v)