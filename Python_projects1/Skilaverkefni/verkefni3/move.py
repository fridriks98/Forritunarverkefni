def texti():
    print("l - for moving left")    #Fall fyrir upplýsingar um hvernig skal færa á x-ásnum
    print("r - for moving right")
    print("Any other letter for quitting")
def breytt():   
    return input("Input your choice: ").lower() #Fall sem tekur inn streng og skilar honum í lágstöfum
def faersla(breyting, new_num): #Færsla fyrir new_num
    if breyting == 'l':
        if new_num == 1:    #Ef jafnt og 1 þá gerist ekkert - 
            new_num = new_num
        else:
            new_num -= 1    #Annars lækkar um 1
    elif breyting == 'r':
        if new_num == 10:   #Ef jafnt og 10 þá gerist ekkert
            new_num = new_num
        else:
            new_num += 1    #Annars hækkar um 1  
    return new_num

tala = int(input("Input a position between 1 and 10: "))
new_num = tala

while 0 < new_num < 11: 
    texti()                                        #Kalla á tvær breytur, texti og breytt
    breyting = breytt()                            #Breytan "breyting" fær gildið á input-inu í fallinu
    if breyting in ('l', 'r'):
        new_num = faersla(breyting, new_num)
        print("New position is:",new_num)
    else: 
        print("New position is:",new_num)
        break