import subprocess

def is_valid_username(username):
    """
    Check if the username contains only letters and numbers.
    This prevents command injection through malicious characters.
    """
    return username.isalnum()

def check_user(username):
    if not is_valid_username(username):
        print("❌ Invalid username! Please use only letters and numbers.")
        return

    try:
        # Safe subprocess call without using shell=True
        subprocess.call(["cmd", "/c", "echo", f"Hello {username}"])
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

def main():
    user = input("Enter username: ")
    check_user(user)

if __name__ == "__main__":
    main()
