import getpass

def main():
    print("Hide-Password-Input")

username = input("Enter Username: ")
password = getpass.getpass("Enter Password: ")

print("\nLogging in...")
print("Username:", username)
print("Password: [hidden for security]")

if __name__ == "__main__":
    main()
