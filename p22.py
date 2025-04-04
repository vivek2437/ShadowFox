# In a village, there is a circular pond with a radius of 84 meters.
# Calculate the area of the pond using the formula: Circle Area = π
# r^2. (Use the value 3.14 for π) Bonus Question: If there is exactly
# 1.4 liters of water in a square meter, what is the total amount of
# water in the pond? Print the answer without any decimal point in
# it. Hint: Circle Area = π r^2 Water in the pond = Pond Area
# Water per Square Meter
r=84
area=3.14*(r**2)
print(area)

#water per square meter
w_p_s_m=1.4
area1=int(w_p_s_m*area)
print("Total amount of water in the pond:", area1, "liters")
