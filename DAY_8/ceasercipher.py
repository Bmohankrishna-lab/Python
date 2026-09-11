# DAY 8: to create a ceaser cipher, we need to shift the letters of the alphabet by a certain number of positions.
alphabet = 'abcdefghijklmnopqrstuvwxyz'
def ceaser(text, shift, encode_or_decode):
    outtext = ''
    if encode_or_decode =='decode':
                shift *= -1
    for i in text:
        if i not in alphabet:
            outtext += i
        else: 
            shifted_index=alphabet.index(i) + shift
            shifted_index %= len(alphabet)  # Wrap around the alphabet 
            outtext += alphabet[shifted_index]
        
    print(f"The {encode_or_decode}d text is {outtext}")
    
    
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == 'no':
        should_continue = False
        print("Goodbye!")
    
    

    
   
ceaser(text, shift, direction)

    