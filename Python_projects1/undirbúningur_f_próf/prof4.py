margfoldunartafla = 1

for margfoldunartafla in range(1,11):                       #Til að fá margföldunartöflur 1-10
    for x in range(1,11):                                   #margfalda hverja töflu með x, þar sem x er 1-10
        print('{:>5}'.format(margfoldunartafla*x),end='')   #geri línuna right justified með breidd 5 og nota end til að hafa töflurnar\
    print(end='\n')                                         #lárettar. Nota end aftur til að búa til nýja línu fyrir\    
                                                            #næstu töflu    