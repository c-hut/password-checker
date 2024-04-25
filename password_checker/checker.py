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
    # Convert the password to lower case and remove non-alphanumeric characters
    alphanumeric_password = ''
    for char in password:
        if char.isalnum():
            alphanumeric_password += char.lower()

    # Check if the alphanumeric password is equal to its reverse using string indexing
    reversed_password = alphanumeric_password[::-1]
    if alphanumeric_password == reversed_password:
        return True
    else:
        return False
               

def evaluate_password_strength(password):
    ''' Assess password strength '''
    if len(password) < 8:
        return "Weak"
    
    if not re.search(r'[a-z]', password) or \
       not re.search(r'[A-Z]', password) or \
       not re.search(r'\d', password) or \
       not re.search(r'[a-zA-Z0-9]', password):
        return 'Weak'
    
    # Check for common patterns
    if has_common_patterns(password) or \
        check_date_patterns(password) or \
        is_palindrome(password):
            return "Weak"

    return "Strong"