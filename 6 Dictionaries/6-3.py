glossary = {
    "Queue": "A collection of elements that follows the First In First Out (FIFO) principle.",
    "Stack": "A collection of elements that follows the Last In First Out (LIFO) principle.",
    "Algorithm": "A step-by-step procedure or formula for solving a problem.",
    "Data Structure": "A way of organizing and storing data so it can be accessed and modified efficiently.",
    "Sorting": "The process of arranging elements in a specific order, typically ascending or descending."
}

# Print the glossary
for term, definition in glossary.items():
    print(f"{term}:\n{definition}\n")
    
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
for name in favorite_languages.keys():
    print(name.title())