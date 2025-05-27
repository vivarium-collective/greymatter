def greet_user(name):
    print(f"Hello, {name}! Welcome to Greymatter.")

def main():
    print("Hello from greymatter!")
    username = input("Enter your username: ")
    greet_user(username)


if __name__ == "__main__":
    main()
