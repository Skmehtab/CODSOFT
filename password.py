#importing random and string
import random
import string

#characters that we are going to use in passowrd
lower=string.ascii_lowercase
upper=string.ascii_uppercase
digits=string.digits
symbols=string.punctuation

def generate_password(length,complexity):
    #defining complexity
    if complexity=="weak":
        all_characters=lower+upper
    elif complexity=="medium":
        all_characters=lower+upper+digits
    elif complexity=="strong":
        all_characters=lower+upper+digits+symbols
    else:
        raise ValueError("Invalid complexity level. Please select from (weak/medium/strong).")
    
    #generating password
    password="".join(random.choice(all_characters) for _ in range(length))
    return password

#get user input for password length and complexity
while True:
    try:
        length=int(input("Enter the desired password length: "))
        
        #checking for minimum length of password
        if length<6:
            print("Minimum 6 characters required. Try again!")
            continue #ask for input again
        
        #taking inputs from user
        complexity_input=input("Enter the desired complexity of password(weak/medium/strong): ").lower()
        password=generate_password(length,complexity_input)
        print("Generated Password: ",password)
        #break from loop if everything is good
        break
    except ValueError as a:
        print(str(a))