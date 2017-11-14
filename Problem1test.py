count = 1000
m = [3, 5, 3*5]
result = 0
Sum = 0
for j in m:
    result = 0
    for i in range(count):
        if i*j < 1000:
            result = result + i*j
        elif i == (count - 1):
            if j < 15:
                Sum = result + Sum
            elif j == 15:
                Sum = Sum - result
                print Sum
		
