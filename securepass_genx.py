import string
import secrets
import re

# Character pools
LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = "!@#$%^&*()_+-=[]{}|;:,.<>?~`"

ALL_CHARACTERS = LOWERCASE + UPPERCASE + DIGITS + SYMBOLS

def generate_password(length=16):
    """Generate a super strong random password"""
    if length < 12:
        print("⚠️  Warning: Passwords shorter than 12 are easy to crack!")
    
    # Guarantee at least one of each type
    password = [
        secrets.choice(LOWERCASE),
        secrets.choice(UPPERCASE),
        secrets.choice(DIGITS),
        secrets.choice(SYMBOLS)
    ]
    
    # Fill the rest randomly
    for _ in range(length - 4):
        password.append(secrets.choice(ALL_CHARACTERS))
    
    # Shuffle to make it unpredictable
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)

def check_strength(password):
    """Calculate strength score (0-10) and give feedback"""
    score = 0
    feedback = []

    # Length bonus
    if len(password) >= 16:
        score += 3
    elif len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("⚠️ Too short! Use at least 12 characters")

    # Character variety
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔤 Add lowercase letters (a-z)")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("🔠 Add uppercase letters (A-Z)")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("🔢 Add numbers (0-9)")

    if re.search(r"[\W_]", password):  # Any special character
        score += 2
    else:
        feedback.append("🔣 Add symbols (!@#$%^&*)")

    # Penalize very common patterns
    common_patterns = ["123", "password", "qwerty", "abc123", "letmein", "111111", "000000"]
    if any(p in password.lower() for p in common_patterns):
        score -= 3
        feedback.append("❌ Avoid common & dangerous patterns!")

    # Keep score between 0 and 10
    score = max(0, min(10, score))
    return score, feedback

def print_fancy_box(title, symbol="★", width=40):
    """Print a beautiful boxed title"""
    print(f"\n{symbol * width}")
    print(f" {symbol} {title.center(width-4)} {symbol} ")
    print(f"{symbol * width}\n")

# ==================== MAIN PROGRAM ====================
print_fancy_box("🔐 SecurePass GenX - Ultimate Password Tool 🔐", "✨")

while True:
    print("╔════════════════════════════════════╗")
    print("║        What would you like to do?  ║")
    print("║   1 → Generate strong password     ║")
    print("║   2 → Check password strength      ║")
    print("║   3 → Exit                         ║")
    print("╚════════════════════════════════════╝")
    
    choice = input("\n➜ Enter your choice (1/2/3): ").strip()

    if choice == "1":
        try:
            length = int(input("➜ How many characters? (12–32 recommended): "))
            if length < 8 or length > 64:
                print("⚠️ Please choose between 8 and 64 characters!")
                continue
        except ValueError:
            length = 16
            print("⚠️ Invalid number → using 16 characters!")

        password = generate_password(length)
        
        print_fancy_box("YOUR NEW SUPER-STRONG PASSWORD", "🔥")
        print(f"  🔑  {password}  🔑")
        print(f"     (Length: {len(password)} characters)\n")
        
        score, tips = check_strength(password)
        
        # Show score with shields
        shields = "🛡️" * (score // 2)
        print(f"   Strength: {score}/10   {shields}")
        
        if score >= 9:
            print("   🌟 GOD MODE PASSWORD – UNBREAKABLE! 🌟")
        elif score >= 7:
            print("   💪 Very strong – hackers will cry! 💪")
        elif score >= 5:
            print("   👍 Not bad – but you can do better!")
        else:
            print("   😟 Weak – change it right now!")
        
        if tips:
            print("\n   Improvement tips:")
            for tip in tips:
                print(f"     • {tip}")

    elif choice == "2":
        password = input("➜ Enter your password to check: ").strip()
        if not password:
            print("❌ You didn't enter anything!")
            continue
        
        print_fancy_box("PASSWORD STRENGTH CHECK", "🔍")
        print(f"  🔑  {password}  🔑\n")
        
        score, tips = check_strength(password)
        
        shields = "🛡️" * (score // 2)
        print(f"   Strength Score: {score}/10   {shields}")
        
        if score == 10:
            print("   🏆 PERFECT – Legendary security level! 🏆")
        elif score >= 8:
            print("   🔥 Extremely strong – great job! 🔥")
        elif score >= 6:
            print("   👍 Decent – room for improvement")
        else:
            print("   ⚠️ Dangerously weak – replace immediately!")
        
        if tips:
            print("\n   How to make it stronger:")
            for tip in tips:
                print(f"     • {tip}")

    elif choice == "3":
        print_fancy_box("Goodbye! Stay Safe Online 🌟", "👋")
        print("   Thanks for using SecurePass GenX!\n")
        break
    
    else:
        print("❓ Please enter only 1, 2 or 3!\n")
    
    print()  # Add some breathing space