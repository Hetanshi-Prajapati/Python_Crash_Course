def build_person(first_name,last_name):
    """Return a dictionary of information about a person."""
    person={'first':first_name,'last':last_name}
    return person
musician=build_person('jimi','hendrix')
print(musician)

print("\n\n")

def build_person1(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person1('jimi', 'hendrix', age=27)
print(musician)
musician = build_person1('jimi', 'hendrix')
print(musician)