a = ['Hello', 'Hi', 'Hey', 'Oyy', 'Oo', 'Heyy']
sent_messages = []

def send_message(messages):
    for message in messages:
        print(f"Sending message: {message}")  # Print the message
        sent_messages.append(message)  # Append the message to sent_messages

# Call the function with a copy of the list 'a'
send_message(a[:])  # Use slicing to pass a copy of the list

# Print the two lists after sending messages
print("\nOriginal messages list:")
print(a)  # This should still contain all the original messages

print("\nSent messages list:")
print(sent_messages)  # This should contain all the sent messages
