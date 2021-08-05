BP = 50000 #Buying price of the property
IR = 1 #Annual interest rate
T = 30 #Time
RIM = 200 #Monthly rental income
RIA = RIM*12
TCA = (RIA/2) #Total costs per year assumed at 50 % of the expected rental income, including repairs, vacancy, ...
AI = ((BP/2)*IR)/100; #Average interest over 30 years
print("On average over the 30 years the annual interest paid will be:")
print(AI)
IBTA= (RIA-TCA) #Income before taxes per year 
TR= 30 #Assumed Tax rate in percent
IATA= (IBTA*TR/100) #Income after taxes per year
print("The expected annual income after the expected taxes would be:")
print(IATA)
