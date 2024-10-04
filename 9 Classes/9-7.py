class user:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        
    def describe_user(self):
        print(f"First_name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        
    def greet_user(self):
        print(f"Hello {self.first_name}!")
        print(f"Hope {self.first_name}, you are fine...")
   
class Admin(user):
    def __init__(self,first_name,last_name,privileges):
        super().__init__(first_name,last_name)
        self.privileges=privileges
        
    def show_privileges(self):
        # privileges=["can add post", "can delete post", "can ban user"]
        for privilege in self.privileges:
            print(f"-{privilege}")
            
person1=Admin('Hetanshi','Prajapati',["can add post", "can delete post", "can ban user"])
person2=Admin('Sagar','Kavaiya',["can add post", "can delete post", "can ban user"])

person1.describe_user()
person1.greet_user()
person1.show_privileges()

print("\n\n")

person2.describe_user()
person2.greet_user()
person2.show_privileges()
