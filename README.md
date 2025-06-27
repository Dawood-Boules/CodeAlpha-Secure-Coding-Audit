# 🔐 CodeAlpha Task 3 – Secure Coding Review with Bandit

✅ Task for CodeAlpha Cyber Security Internship  
👨‍💻 Submitted by: **Dawood**

---

## 📌 Objective

This task involved performing a secure code review and static analysis on a sample Python script (`login.py`) to identify security vulnerabilities and apply remediations following secure coding practices.

---

## 🛠️ Tools Used

- **Python 3.13.2**
- **Bandit v1.8.3** – Static security analyzer for Python
- **Visual Studio Code** – Code editor
- **Windows 10** – Development platform

---

## 🔍 Key Findings (from `bandit_output.txt`)

| Issue Code | Description                                               | Severity |
|------------|-----------------------------------------------------------|----------|
| B404       | Use of subprocess module can pose security risks         | Low      |
| B602       | Use of `shell=True` with user input (Command Injection)  | High     |
| B603       | Insecure subprocess usage without shell=True             | Low      |
| B607       | Partial executable path in subprocess call               | Low      |

---

## 🛡️ Original Code Issue

The original code used `subprocess.call()` with `shell=True` and raw user input:

```python
subprocess.call(f"echo Hello {username}", shell=True)

This is dangerous because it lets the user inject system commands.

---

## ✅ Fixed (Secure) Version

```python
import subprocess

def is_valid_username(username):
    return username.isalnum()

def check_user(username):
    if not is_valid_username(username):
        print("Invalid username! Use only letters and numbers.")
        return
    subprocess.call(["cmd", "/c", "echo", f"Hello {username}"])

def main():
    user = input("Enter username: ")
    check_user(user)

---

## ✅ Summary of Improvements
- ✅ Removed `shell=True` to prevent command injection
- ✅ Added input validation using `isalnum()`
- ✅ Used subprocess with a safe list format instead of string commands

---

## 📁 Files in This Repository

| File Name         | Description                                  |
|------------------|----------------------------------------------|
| `login.py`        | The original vulnerable script               |
| `login_fixed.py`  | The secure version with best practices       |
| `bandit_output.txt` | Bandit scan result (optional but recommended) |
| `task3_report.pdf` | Full audit report with explanation (your PDF) |

---

## 📌 How to Run Bandit

You can scan your code using Bandit like this:

```bash
pip install bandit
bandit login.py


if __name__ == "__main__":
    main()

