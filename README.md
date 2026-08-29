# Password Strength Analyzer — ThinAnex Internship Task

A comprehensive password security evaluation tool built with Python and Flask. This project analyzes user-entered passwords against length, character diversity, common patterns, and mathematical entropy while suggesting secure alternatives and preventing credential reuse.

---

## 🛠️ Tech Stack & Concepts

- **Language:** Python 3.8+
- **Web Framework:** Flask
- **Database:** SQLite
- **Security & Cryptography:** `bcrypt` (password hashing), `secrets` (cryptographically secure generation), Shannon Entropy calculation ($E = L \log_2(R)$)

---

## ✨ Features

- **Length & Complexity Scoring:** Checks minimum length standards and requires a mix of uppercase, lowercase, numerical, and special characters.
- **Pattern Detection & Entropy:** Penalizes common sequences (e.g., `12345`, `qwerty`) and calculates bit entropy to measure theoretical unpredictability.
- **Secure Password Suggestions:** Uses Python's `secrets` module to generate memorable passphrases and high-entropy random keys.
- **Password History & Reuse Prevention:** Hashes credentials using `bcrypt` and stores them in SQLite to prevent users from reusing past passwords.

---

## 🚀 Setup & Installation Instructions

Follow these steps to run the application locally on your machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/venkatadri2007manchu-lgtm/password-strength-analyzer.git](https://github.com/venkatadri2007manchu-lgtm/password-strength-analyzer.git)
cd password-strength-analyzer

🚀 **Live Demo:** [https://password-strength-analyzer-43vb.onrender.com](https://password-strength-analyzer-43vb.onrender.com)