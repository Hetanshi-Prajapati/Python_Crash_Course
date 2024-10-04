message = input("Tell me something, and I will repeat it back to you: ")
print(message)

print("\n\n")

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

print("\n\n")

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")
# the operator += takes the string that was assigned to prompt and adds the new string onto the end.