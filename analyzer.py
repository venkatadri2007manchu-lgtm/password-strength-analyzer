import math
import re

COMMON_PATTERNS = ["12345", "qwerty", "password", "admin", "letmein", "welcome"]

def calculate_entropy(password: str) -> float:
    pool_size = 0
    if re.search(r"[a-z]", password): pool_size += 26
    if re.search(r"[A-Z]", password): pool_size += 26
    if re.search(r"\d", password): pool_size += 10
    if re.search(r"[^a-zA-Z0-9]", password): pool_size += 32
    
    if pool_size == 0 or len(password) == 0:
        return 0.0
    
    return len(password) * math.log2(pool_size)

def evaluate_password(password: str) -> dict:
    feedback = []
    score = 0
    
    if len(password) < 8:
        feedback.append("Increase length to at least 8 characters.")
    elif len(password) >= 12:
        score += 2
    else:
        score += 1

    if not re.search(r"[a-z]", password): feedback.append("Include lowercase letters.")
    else: score += 1

    if not re.search(r"[A-Z]", password): feedback.append("Include uppercase letters.")
    else: score += 1

    if not re.search(r"\d", password): feedback.append("Include numbers.")
    else: score += 1

    if not re.search(r"[^a-zA-Z0-9]", password): feedback.append("Include special characters.")
    else: score += 1

    for pattern in COMMON_PATTERNS:
        if pattern in password.lower():
            score -= 2
            feedback.append(f"Avoid common pattern: '{pattern}'")

    entropy = calculate_entropy(password)

    if score >= 5 and entropy >= 60:
        strength = "Strong"
    elif score >= 3 and entropy >= 40:
        strength = "Moderate"
    else:
        strength = "Weak"

    return {
        "score": max(0, score),
        "entropy": round(entropy, 2),
        "strength": strength,
        "feedback": feedback
    }