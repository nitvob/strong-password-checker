import random
import string

def is_strong_password(password: str) -> bool:
    """
    Check if the provided password meets the following criteria:
    - Minimum length of 8 characters
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one number
    - Contains at least one special character
    - Maximum length of 100 characters
    
    Args:
        password (str): The password to check
        
    Returns:
        bool: True if password meets all criteria, False otherwise
    """
    # TODO: Implement the password checking logic here
    def isspecial(char):
        '''
        special means NOT lowercase letter AND NOT uppercase letter AND NOT digit 
        not char.islower() && not char.isupper() && not char.isdigit()
        '''
        if not char.islower() and not char.isupper() and not char.isdigit():
            return True
        else: 
            return False 

    if len(password) < 8:
        return False
    elif len(password) > 100: 
        return False
    elif not any(char.islower() for char in password): 
        return False
    elif not any(char.isupper() for char in password):
        return False 
    elif not any(char.isdigit() for char in password): 
        return False
    elif not any(isspecial(char) for char in password):
        return False
    else:
        return True
        


def generate_strong_password(length: int) -> str:
    """
    Generate a strong password that meets all the criteria:
    - Contains uppercase letters
    - Contains lowercase letters
    - Contains numbers
    - Contains special characters
    
    Args:
        length (int): Length of the password to generate
        
    Returns:
        str: A strong password meeting all criteria
    """
    # TODO: Implement the password generation logic here
    '''
    what if the length they give us is <8 or >100, riase an error
    get a random lowercase letter. stick this into the string
        how do we get a random lowercase letter (google it)
    get a random uppercase letter. stick this into the string
        how do we get a random uppercase letter (google it)
    get a random digit. stick this into the string
        how do we get a random digit (random.randint(0, 9))
    get a random special. stick this into the string
    
    what about length - 4 remaing chars?
        put random chars for the rest
    '''
    if length < 8 or length > 100: 
        raise ValueError("Invalid length")
    
    randomLower = random.choice(string.ascii_lowercase)
    randomUpper = random.choice(string.ascii_uppercase)
    randomDig = str(random.randint(0, 9))
    randomSpecial = random.choice(string.punctuation)
    
    password = randomLower + randomUpper + randomDig + randomSpecial 

    for i in range(length - 4):
        randomLower = random.choice(string.ascii_lowercase)
        randomUpper = random.choice(string.ascii_uppercase)
        randomDig = str(random.randint(0, 9))
        randomSpecial = random.choice(string.punctuation)
        randomChar = random.choice([randomLower, randomUpper, randomDig, randomSpecial])
        password += randomChar

    return password
    

        
   