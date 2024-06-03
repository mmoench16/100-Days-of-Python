from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
active = True

print(logo)

def caesar(direction, text, shift):
    cypher = ""

    if direction == "decode":
        shift *= -1

    for c in text:

        if c not in alphabet:
            cypher += c
        else:
            index = alphabet.index(c) + shift
            
            if index >= len(alphabet):
                cypher += alphabet[index - len(alphabet)]
            elif index < 0:
                cypher += alphabet[index + len(alphabet)]
            else:
                cypher += alphabet[index]

    print(f"The {direction}d text is {cypher}")

while active:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(direction, text, shift)

    again = input("Would you like to encode/decode another message? Type 'yes' or 'no'.\n")
    if again == "no":
        active = False
        print("Goodbye.")