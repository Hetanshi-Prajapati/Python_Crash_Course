name=['A','B','C']
for i in name:
    print(f"Hi,{i},")
    print(f"I am inviting you for the dinner")
    
print(f"{name[1]} is not come on dinner")

name[1]='D'

for i in name:
    print(f"Hi,{i},")
    print(f"I am inviting you for the dinner")


for i in name:
    print(f"{i}")
    
print("\n\n")
name.insert(0,'E')
for i in name:
    print(f"{i}")
    
print("\n\n")
name.insert(2,'F')
for i in name:
    print(f"{i}")
    
print("\n\n")
name.append('G')
for i in name:
    print(f"{i}")
    
print("\n\n") 
abc=name.pop()
print(f"{abc},  I can not invite you. bcz of some problems")

print("\n\n")
ghi=name.pop(1)
print(f"{ghi},  I can not invite you. bcz of some problems")

print("\n\n")
for i in name:
    print(f"{i}")
    
print("\n\n")
del name[0]
del name[1]

print("\n\n")
for i in name:
    print(f"{i}")