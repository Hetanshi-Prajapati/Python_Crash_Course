class user:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=0
        
    def describe_user(self):
        print(f"First_name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        
    def greet_user(self):
        print(f"Hello {self.first_name}!")
        print(f"Hope {self.first_name}, you are fine...")
        
    def increment_login_attempts(self):
        self.login_attempts=self.login_attempts+1
      
    def reset_login_attempts(self):
        self.login_attempts=0
          
person1=user('Hetanshi','Prajapati')
person2=user('Sagar','Kavaiya')

person1.describe_user()
person1.greet_user()
person1.increment_login_attempts()
print(f"Login attempts: {person1.login_attempts}")
person1.reset_login_attempts()
print(f"Login attempts after reset: {person1.login_attempts}")
print("\n\n")

person2.describe_user()
person2.greet_user()
person2.increment_login_attempts()
print(f"Login attempts: {person2.login_attempts}")
person2.reset_login_attempts()
print(f"Login attempts after reset: {person2.login_attempts}")