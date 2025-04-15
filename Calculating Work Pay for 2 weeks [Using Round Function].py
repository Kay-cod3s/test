hoursweekone = float(input("How many hours did you work in the first week??? "))
hoursweektwo = float(input("How about week two?? "))
wage = float(input("How much do you make an hour? "))
totalhours = (hoursweekone + hoursweektwo)
total = totalhours * wage
roundedtotal= round(total , 2)
print(str(roundedtotal) +" This is how much you earned working " + str(totalhours) + " Hours  at an hourly wage of " + str(wage))  
