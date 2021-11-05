def valid_email(mail):
    if "@" in mail:
        if "." in mail:
            return True
        else:
            return False
    elif "." in mail:
        return False
    else:
        return False

email = input("Please enter your email: ")

print(valid_email(email))

        

