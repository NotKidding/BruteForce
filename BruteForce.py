import string;

passkey = ''
found = False

def bruteForce(attempt='', length=1):
    global found
    chars = string.ascii_letters + string.digits + string.punctuation
    if len(attempt) == length:
        print(f"Trying attempt: {attempt}")
        if attempt == passkey:
            print(f"\nPasskey found: {attempt}")
            found = True
        return
    for char in chars:
        if found:
            break
        bruteForce(attempt+char, length)

def findPasskey():
    if passkey == '':
        print("Input Required")
        return
    length = 1
    while not found:
        print(f"\nTrying length: {length} \n")
        bruteForce(length=length)
        length += 1

def main():
    global passkey
    passkey = input("Enter Passkey:")
    findPasskey()

if __name__ == "__main__":
    main()