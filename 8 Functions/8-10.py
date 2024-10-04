messages=['Hello','Hi','Hey','Oyy','Oo','Heyy']
sent_messages=[]

def send_message(message_list,sent_list):
    while message_list:
        current_message=message_list.pop(0)
        print(f"Sending message: {current_message}")
        sent_list.append(current_message)
"""for i in range(len(a)):  # Loop through the list using its length
        message = a.pop()  # Pop the last message from the list 'a'
        print(f"Sending message: {message}")  # Print the message
        sent_messages.append(message)  # Append the popped message to sent_messages"""
send_message(messages, sent_messages)

# Display the two lists after sending messages
print("\nMessages list after sending:")
print(messages)  # Should be empty

print("\nSent messages list:")
print(sent_messages)  # Should contain all the sent messages

