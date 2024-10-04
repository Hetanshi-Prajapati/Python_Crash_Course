favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
   print(language.title())
   
print("\n\n")
for language in set(favorite_languages.values()): #set is use to remove duplication items
   print(language.title())