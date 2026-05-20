def encrypt(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def decrypt(message, shift):
    return encrypt(message, -shift)


def display_table(message, shift):
    print("\n  Original → Encrypted")
    print("  " + "-" * 22)
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted = chr((ord(char) - base + shift) % 26 + base)
            print(f"     {char}    →    {encrypted}")
    print()


def main():
    print("\n" + "=" * 40)
    print("       🔐 Caesar Cipher Tool")
    print("=" * 40)

    while True:
        print("\n  [1] Encrypt a message")
        print("  [2] Decrypt a message")
        print("  [3] Quit")

        choice = input("\n  Choose an option: ").strip()

        if choice == '3':
            print("\n  Goodbye! 👋\n")
            break

        elif choice in ['1', '2']:
            message = input("  Enter your message: ").strip()

            if not message:
                print("  ❌ Message cannot be empty.")
                continue

            try:
                shift = int(input("  Enter shift number (1-25): ").strip())
                if not 1 <= shift <= 25:
                    print("  ❌ Shift must be between 1 and 25.")
                    continue
            except ValueError:
                print("  ❌ Please enter a valid number.")
                continue

            if choice == '1':
                output = encrypt(message, shift)
                print(f"\n  ✅ Encrypted: {output}")
                display_table(message, shift)

            else:
                output = decrypt(message, shift)
                print(f"\n  ✅ Decrypted: {output}")

        else:
            print("  ❌ Invalid option. Choose 1, 2 or 3.")


if __name__ == "__main__":
    main()
