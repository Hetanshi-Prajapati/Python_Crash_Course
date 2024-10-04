favourite_places={
    'Alice': ['Paris', 'New York', 'Tokyo'],
    'Bob': ['Sydney', 'Amsterdam'],
    'Charlie': ['Rome', 'Berlin', 'Venice']
}

for person, places in favourite_places.items():
    print(f"{person}'s favorite places are:")
    for place in places:
        print(f"- {place}")