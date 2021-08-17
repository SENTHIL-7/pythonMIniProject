# Problem :
# Develop a Java application to generate Electricity bill. Create a class with the following
# members: Consumer no., consumer name, previous month reading, current month reading, type of
# EB connection (i.e domestic or commercial). Compute the bill amount using the given tariff.
# If the type of the EB connection is domestic, calculate the amount to be paid as follows:
# • First 100 units - Rs. 1 per unit
# • 101-200 units - Rs. 2.50 per unit
# • 201 -500 units - Rs. 4 per unit
# • > 501 units - Rs. 6 per unit
# If the type of the EB connection is commercial, calculate the amount to be paid as follows:
# • First 100 units - Rs. 2 per unit
# • 101-200 units - Rs. 4.50 per unit
# • 201 -500 units - Rs. 6 per unit
# • > 501 units - Rs. 7 per unit

#************************************************************************************************

consumerNo = int(input("Enter Consumer No : "))
consumerName = input("Enter Consumer Name : ")
prev_Month_reading =int(input('Enter Previous Month Reading : '))
currect_Month_reading =int(input('Enter Current Month Reading : '))
print("Enter Type of EB Connections : <domestic or commercial>")
TypeOfEB = input()


print("-------------------------------ELECTRICITY BILL-----------------------------------------")
print("Consumer Name : " + consumerName)
Units = currect_Month_reading - prev_Month_reading
print(f"NUmber of units : {Units}" )

pay=0
if(TypeOfEB.lower()=="domestic"):
    if(Units<=100):
        pay=Units*1

    elif((Units>=101) & (Units<=200)):
        pay=(100*1)+((Units-100) *2.50)   

    elif((Units>=201) & (Units<=500)): 
        pay=((100*1)+(100*2.50)+((Units-200) * 4))

    elif(Units>500): 
        pay=(100*1)+(100 *2.50) + (300*4) + ((Units -500) * 6)    
         
elif(TypeOfEB.lower()=="commercial"):
    if(Units<=100):
        pay=Units*2

    elif((Units>100) & (Units<=200)):
        pay=(100*2)+((Units-100) *4.50)   

    elif((Units>200) & (Units<=500)): 
        pay=(100*2)+(100 *4.50) +((Units -200) * 6)    

    elif(Units>500): 
        pay=(100*2)+(100 *4.50) + (300*6) + ((Units -500) * 7)    



else:
    print("type is incorrect.")
print(f"Amount to be paid is : Rs.{pay}")
print("\n----------------------------------------------------------------------------------------")


