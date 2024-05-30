alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# def encrypt(text, shift):
    
#     cypher = ""

#     for c in text:
#         index = alphabet.index(c) + shift
#         if index >= len(alphabet):
#             cypher += alphabet[index - len(alphabet)]
#         else:
#             cypher += alphabet[index]

#     print(f"The encoded text is {cypher}")

# def decrypt(text, shift):
    
#     cypher = ""

#     for c in text:
#         index = alphabet.index(c) - shift
#         if index < 0:
#             cypher += alphabet[index + len(alphabet)]
#         else:
#             cypher += alphabet[index]

#     print(f"The encoded text is {cypher}")

def caesar(direction, text, shift):
    cypher = ""
    original_shift = shift

    for c in text:
        if direction == "decode":
            shift = original_shift * -1
            
        index = alphabet.index(c) + shift
        
        if index >= len(alphabet):
            cypher += alphabet[index - len(alphabet)]
        elif index < 0:
            cypher += alphabet[index + len(alphabet)]
        else:
            cypher += alphabet[index]

    print(f"The {direction}d text is {cypher}")

caesar(direction, text, shift)