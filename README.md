# 🔐 CodeAlpha Task 3 – Secure Coding Review with Bandit

✅ Task for CodeAlpha Cyber Security Internship  
👨‍💻 Submitted by: **Dawood**

---

## 📌 Objective

This task involved performing a secure code review and static analysis on a Python script (`login.py`) to identify security vulnerabilities, analyze risks, and fix the code using secure coding best practices.

---

## 🛠️ Tools Used

- **Python 3.13.2**
- **Bandit v1.8.3** – Static security analyzer for Python
- **Visual Studio Code**
- **Windows 10**

---

## 🔍 Key Findings (from Bandit)

| Issue Code | Description                                               | Severity |
|------------|-----------------------------------------------------------|----------|
| B404       | Use of `subprocess` module can pose security risks       | Low      |
| B602       | Use of `shell=True` with user input (Command Injection)  | High     |
| B603       | Insecure subprocess usage without `shell=True`           | Low      |
| B607       | Partial executable path in subprocess call               | Low      |

---

## 🛡️ Original Code Issue

The original script allowed command injection by using `subprocess.call()` with `shell=True` and raw user input:

```python
import subprocess

username = input("Enter your username: ")
subprocess.call(f"echo Hello {username}", shell=True)
