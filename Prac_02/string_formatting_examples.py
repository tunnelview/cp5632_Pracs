name = "Gibson L-5 CES"
year = 1922
cost = 16035.4

#1922 Gibson L-5 CES for about $16,035!

print("{:>2} {} for about ${:,.0f}!".format(year,name,cost))


#Starting Point = 0
#Ending Point = N-1 (means the last digit -1) 101-1=100
# Step - The number with which the increment is happening

for i in range (0,151,50):
    print("{:>3}".format(i))