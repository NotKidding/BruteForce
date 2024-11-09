import string
import sys

passkey = ''
found = False
try_count = 0
def bruteForce(attempt='', length=1):
    global found, try_count
    chars = string.ascii_letters + string.digits + string.punctuation
    if len(attempt) == length:
        sys.stdout.write(f"\rTrying attempt: {attempt}")
        sys.stdout.flush()
        try_count += 1
        if attempt == passkey:
            print(f"\n\nPasskey found: {attempt}")
            print(f"Total tries: {try_count}")
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
        bruteForce(length=length)
        length += 1

def main():
    global passkey
    passkey = input("Enter Passkey:")
    findPasskey()

if __name__ == "__main__":
    main()
