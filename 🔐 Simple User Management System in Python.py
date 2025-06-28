class User:
    def __init__(self, username, password, store):
        self.username = username
        self.password = password
        self.store = store

    def login(self):
        for user in self.store:
            if user[0] == self.username and user[1] == self.password:
                return "✅ Logged in successfully"
        return "❌ Invalid username or password"

class Admin(User):
    def __init__(self, username, password, store):
        super().__init__(username, password, store)

    def delete_user(self):
        for i in range(len(self.store)):
            if self.store[i][0] == self.username:
                attempt = input("⚠️ Enter password to confirm deletion or type 'n' to cancel: ")
                while attempt != 'n' and attempt != self.password:
                    attempt = input("❌ Wrong password. Try again or type 'n' to cancel: ")

                if attempt == self.password:
                    self.store.pop(i)
                    return "✅ Successfully deleted user"
                else:
                    return "❌ Deletion canceled"
        return "❌ User not found"

    def add_user(self):
        new_user = [self.username, self.password]
        self.store.append(new_user)

    def display(self):
        if not self.store:
            print("📭 No users found.")
        else:
            print("\n📋 Registered Users:")
            for i, user in enumerate(self.store, start=1):
                print(f"{i}. Username: [{user[0]}], Password: [{user[1]}]")
        print()

# Initialize user storage
user_store = []

# Helper function
def get_info():
    name = input("Enter username: ")
    password = input("Enter password: ")
    return name, password

# Main loop
while True:
    service = input("""
Select a service:
1 - Log In
2 - Sign Up
3 - Delete Account
4 - Display All Users
5 - Exit
> """).strip()

    if service == '1':
        username, password = get_info()
        user = Admin(username, password, user_store)
        print(user.login())

    elif service == '2':
        username, password = get_info()
        user = Admin(username, password, user_store)
        user.add_user()
        print("✅ User added successfully")

    elif service == '3':
        username, password = get_info()
        user = Admin(username, password, user_store)
        print(user.delete_user())

    elif service == '4':
        admin = Admin('', '', user_store)
        admin.display()

    elif service == '5':
        print("👋 Exiting program.")
        break

    else:
        print("❌ Invalid option. Please try again.")
