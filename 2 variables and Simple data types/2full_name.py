#using variables in string

first_name="ada"
last_name="lovelace"
full_name=f"{first_name} {last_name}"
print(full_name) #join both string

print(f"Hello, {full_name.title()}!")#title do the first letter capital

message=print(f"Hello, {full_name.title()}!")
print(message)