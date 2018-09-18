#Fall fyrir upplýsingar um hvernig skal færa á x-ásnum
def texti():
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")
#Fall sem tekur inn streng og skilar honum í lágstöfum
def breytt():
    return input("Input your choice: ").lower()
#Færsla fyrir new_num == 1
def faersla(breyting, new_num):
    if breyting == 'l':
        new_num = new_num
    elif breyting == 'r':
        new_num += 1
    return new_num
#Færsla fyrir new_num == 10
def faersla1(breyting,new_num):
    if breyting == 'l':
        new_num -= 1
    elif breyting == 'r':
        new_num = new_num
    return new_num
#Færsla fyrir restina af tölunum á bilinu
def faersla2(breyting,new_num):
    if breyting == 'l':
        new_num -= 1
    elif breyting == 'r':
        new_num += 1
    return new_num

tala = int(input("Input a position between 1 and 10: "))
new_num = tala

while 0 < new_num < 11: 
    texti()                                        #Kalla á tvær breytur, texti og breytt
    breyting = breytt()                            #Breytan "breyting" fær gildið á input-inu í fallinu

    if breyting == 'l' or breyting == 'r':
        if new_num == 1:
            new_num = faersla(breyting,new_num)    #Keyrir fallið fyrir new_num == 1
        elif new_num == 10:
            new_num = faersla1(breyting,new_num)   #Keyrir fallið fyrir new_num == 10
        else:    
            new_num = faersla2(breyting,new_num)   #Keyrir fallið fyrir new_num == 2-9

        print("New position is:",new_num)          #Eftir hverja keyrslu prentast út nýja gildið á new_num
        
    else:                                          #Eftir slegið er inn annað en l eða r í breytt fallinu\
        print("New position is:",new_num)          #Prentast út sama gildi og var síðast og síðan breakar forritið\
        break                                      #út úr loopunni
                                                   