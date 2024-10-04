rivers={
    'nile':'egypt',
    'Ganga':'India',
    'Yamuna':'Dubai',
}

for river,country in rivers.items(): #items print  both keys and value
    print(f"The {river.title()} runs through {country.title()}.")
    
print("\n\n")

for river in rivers.keys(): #keys print keys
    print(river.title())
    
print("\n\n")

for river in rivers.values(): #value print value
    print(river.title())