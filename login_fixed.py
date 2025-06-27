import subprocess

def is_valid_username(username):
    return username.isalnum()

def check_user(username):
    if not is_valid_username(username):
        print("❌ Invalid username! Use only letters and numbers.")
        return
    try:
        subprocess.call(["cmd", "/c", "echo", f"Hello {username}"])
    except Exception as e:
        print(f"⚠️ Error: {e}")

def main():
    user = input("Enter username: ")
    check_user(user)

if __name__ == "__main__":
    main()
