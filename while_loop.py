n = int(input("Enter a number: "))

sum_total = 0
current_number = 1

while current_number <= n:
    sum_total += current_number  
    current_number += 1          
    
print(f"The sum of the first {n} numbers is: {sum_total}")