current_users=['A','B','C','J','K']
new_users=['G','H','I','J','K']

current_users_lower=[current_user.lower() for current_user in current_users]
new_users_lower=[new_user.lower() for new_user in new_users]

for new_user_lower in new_users_lower:
    if new_user_lower in current_users_lower:
        print("Enter new user name: ")
    else:
        print(f"The username {new_users} is available")
