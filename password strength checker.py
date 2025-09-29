import re 

def check_password_strength(password):
    if len(password) < 8:
        return "Your Password must contain at least 8 characters"
    
    elif re.search('[0-9]', password) is None:
        return "Your Password must contain at least one number"
    
    elif re.search('[A-Z]', password) is None:
        return "Your Password must contain at least one uppercase letter"
    
    elif re.search('[a-z]', password) is None:
        return "Your Password must contain at least one lowercase letter"
    
    elif not re.search("[@#$%^&*!]", password):
        return "Your Password must contain at least one special character"
    
    return "Your Password is strong"

def password_checker():
    print("Welcome to Password Strength Checker") 

    while True:
        password = input("Enter your password (or type 'Exit' to quit): ")

        if password.lower() == 'exit':
            print("Thanks for using this tool!")
            break
        
        result = check_password_strength(password)
        print(result)

#Run the checker
if __name__ == "__main__":
    password_checker()
