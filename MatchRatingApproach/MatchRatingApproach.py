def encode(name):
    name= name.upper()
    name = "".join([name[0]] + [c for c in name[1:] if c not in "AEIOU"])
    return "".join(sorted(set(name), key = name.index))

def compareNames(name1, name2):
    name1 = encode(name1)
    name2 = encode(name2)
    
    len_name1 =  len(name1)
    len_name2 =  len(name2)
    
    if abs(len_name1 - len_name2) > 3:
        return False
    
    min_len = min(len_name1, len_name2, 3)
    
    for i in range(min_len):
        if name1[i] != name2[i]:
            return False
    
    return True

#Encode names:
while True:
    last_name = input("Enter a last name or type 'quit' to exit: ")
    if last_name.lower == "quit":
        exit()
    
    encoded_name =  encode(last_name)
    print(f"The encoded name is: {encoded_name}")