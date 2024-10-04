favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
people_to_poll=['jen','sarah','edwad','phil']
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title}, for taking the poll")
    else:
        print(f"{person.title()},we invite you to take the favourite languages poll!")