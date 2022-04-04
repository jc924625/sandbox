"""
description:A simple password cheacker
name : johns

"""


def is_valid_password(text):
    """check whether a given text has the correct password format"""
    return 8 <= len(text) <= 20 and "*" in text

def main():
    """start program"""
    new_password = "helloworld"
    print(f"{new_password} is a valid password? {is_valid_password(new_password)}")

if __name__ == '__main__':
    main()
