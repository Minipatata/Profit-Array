import array as arr
prices=arr.array('i',[635,864,247,325,257,745,245])
profit=0
for i in range(1,len(prices)):
    if prices[i]>prices[i-1]:
        profit=profit+(prices[i]-prices[i-1])
print(profit)