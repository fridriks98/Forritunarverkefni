start = input("Initial value: ")
step = input("Step: ")

start_int = int(start)
step_int = int(step)

the_sum = 0

while the_sum < 100:
    the_sum += start_int
    print(start_int, end=' ') 
    start_int = start_int + step_int

print()
print("The sum of series:",the_sum)
        
