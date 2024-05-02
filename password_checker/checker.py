import re

# Establish common password patterns
COMMON_PASSWORD_PATTERNS = [
    r'password',
    r'password1',
    r'abc123',
    r'000000',
    r'111111',
    r'1234',
    r'123123',
    r'12345'
    r'123456',
    r'12345678',
    r'123456789',
    r'1234567890',
    r'27653',
    r'654321',
    r'qwerty',
    r'qwert123',
    r'qwertyuiop',
    r'asdfghjkl',
    r'1q2w3e4r',
    r'1q2w3e4r5t',
    r'zaq12wsx',
    r'iloveyou',
    r'dragon',
    r'sunshine',
    r'princess',
    r'letmein',
    r'monkey',
    r'kitty',
    r'superman',
    r'red',
    r'blue',
    r'black',
    r'gold',
    r'green',
    r'pink',
    r'white',
    r'brown',
    r'silver',
    r'grey',
]

def has_common_patterns(password):
    ''' Check for common patterns '''
    for pattern in COMMON_PASSWORD_PATTERNS:
        if re.search(pattern, password, re.IGNORECASE):
            return True
    return False

def check_date_patterns(password):
    ''' Determine whether or not dates have been used '''
    date_patterns = [
        # DD/MM/YYYY or MM/DD/YYYY
        r'\d{1,2}/\d{1,2}/\d{4}',
        # YYYY/MM/DD or YYYY/DD/MM
        r'\d{4}/\d{1,2}/\d{1,2}',
        # DD-MM-YYYY or MM-DD-YYYY
        r'\d{1,2}-\d{1,2}-\d{4}',
        # YYYY-MM-DD or YYYY-DD-MM
        r'\d{4}-\d{1,2}-\d{1,2}',
        # DD.MM.YYYY or MM.DD.YYYY
        r'\d{1,2}.\d{1,2}.\d{4}',
        # YYYY.MM.DD or YYYY.DD.MM
        r'\d{4}.\d{1,2}.\d{1,2}'
    ]
    
    for pattern in date_patterns:
        if re.search(pattern, password):
            return True
    return False

def is_palindrome(password):
    ''' Determine whether or not the password is a palindrome '''
    alpha_password = ''.join(char.lower() for char in password if char.isalpha())
    return alpha_password == alpha_password[::-1]
               
def evaluate_password_strength(password):
    ''' Assess password strength '''
    if len(password) < 8:
        return "Weak"
    
    if is_palindrome(password):
        return "Weak"
    
    if check_date_patterns(password):
        return "Weak"
    
    criteria_met = 0
    
    if re.search(r'[A-Z]', password):
       criteria_met += 1
    if re.search(r'\d', password):
       criteria_met += 1
    if re.search(r'[^a-zA-Z0-9]', password):
        criteria_met += 1
    
    if criteria_met == 1:
        return "Weak"
    elif criteria_met == 2:
        return "Medium"
    elif criteria_met == 3:
        return "Strong"
    else: return "Weak"