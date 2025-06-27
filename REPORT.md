# 📄 Secure Code Review – Task 3 Report
**Submitted by:** Dawood  
**Domain:** Cyber Security  
**Internship:** CodeAlpha

---

## 🔍 Objective

This task required analyzing a Python script (`login.py`) for security issues using the Bandit tool and applying best practices to fix the code.

---

## 🛡️ Identified Issues

- Use of `subprocess.call()` with `shell=True`
- No input validation (user input passed directly to shell)

These issues can allow command injection and are flagged by Bandit as high-risk.

---

## ✅ Fix Summary

- Removed `shell=True`
- Added `isalnum()` validation to sanitize user input
- Used subprocess with a safe list format
- Wrapped subprocess in a `try-except` block

---

## 📌 Tools Used

- Python 3.13.2
- Bandit v1.8.3
- Visual Studio Code
- Windows 10

---

## 🧪 Final Result

The fixed version of the script passed the Bandit scan with no high-risk issues.

---

✅ Task Completed as part of the **CodeAlpha Cyber Security Internship**
