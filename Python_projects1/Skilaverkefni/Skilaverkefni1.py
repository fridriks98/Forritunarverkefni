loan = int(input("Input the cost of the of the item in $: "))
payment = 50.0

month = 0
total_interest_paid = 0

if 0 < loan < 2500: 
    if loan > 1000:
        percent = 0.02
    else:
        percent = 0.015
    while loan > 0:
        month += 1
        interest_paid = loan * percent
        interest_paid = round(interest_paid,2)
        if loan < payment:
            payment = loan + (loan * percent)
            payment = round(payment,2)
        actual_payment = payment - (interest_paid)
        actual_payment = round(actual_payment,2)  
        loan -= actual_payment
        loan = round(loan,2)
        print("Month:", month, "Payment:",payment, \
        "Interest paid:",interest_paid, "Remaining debt:"\
        ,loan)
            
        total_interest_paid += interest_paid                
    
    print("Number of Months:",month)
    print("Total interest paid:",round(total_interest_paid,2))        

else:
    print("That amount or payment is not available")