cities={
    'Delhi':{
        'country':'France',
        'population':2148000,
        'fact':'Paris is known s the "City of Light".'
    },
    'Pune':{
        'country': 'Japan',
        'population': 13929000,
        'fact': 'Tokyo is the largest metropolitan area in the world.'
    },
    'Banglore':{
        'country': 'USA',
        'population': 8419600,
        'fact': 'New York is known as "The Big Apple".'
    }
}

for city, info in cities.items():
    print(f"City: {city}")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")