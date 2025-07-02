def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            base = ord('A') if char.isupper() else ord('a')
            if mode == "encrypt":
                result += chr((ord(char) - base + shift_amount) % 26 + base)
            elif mode == "decrypt":
                result += chr((ord(char) - base - shift_amount) % 26 + base)
        else:
            result += char
    return result

def main():
    print("=== Caesar Cipher Tool ===")
    mode = input("Do you want to encrypt or decrypt? (enter 'encrypt' or 'decrypt'): ").strip().lower()
    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (e.g., 3): "))
        output = caesar_cipher(message, shift, mode)
        print(f"\nResult: {output}")
    except ValueError:
        print("Please enter a valid integer for the shift.")

if __name__ == "__main__":
    main()