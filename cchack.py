HASH = "yeezy"
print("The hash is %s" % HASH)
Password = input("What is the password? ")

KEY = 13
i = 0
correct = True
while i < len(HASH):
    if len(HASH) != len(Password):
        print("The password is not the correct length.")
        correct = False
        break
    ascii_val = ord(Password[i]) # grab the ascii val of the letter
    new_ascii_val = ascii_val + KEY # add the key to the ascii val
    while new_ascii_val > 122: # make sure the ascii val is between 96 and 122
        new_ascii_val -= 26
    if chr(new_ascii_val) == HASH[i]:
        print("Character at space %d is correct." % i)
    else:
        print("Character at space %d is incorrect." %i)
        correct = False
    i += 1

if correct == True:
    print("Password accepted, access granted.")
else:
    print("Password declined, access denied.")
