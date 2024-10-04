peoples={
    # 'names':['Hetanshi','Sagar','Priyal','Parth','Nevil']
    'Hetanshi':19,
    'Sagar':20,
    'Priyal':21,
    'Parth':22,
    'Nevil':23
}
for key,value in peoples.items():
    print(f"{key.title()}:{value}")
    
print("\n\n")

for name in peoples.keys():
    print(name.title())
