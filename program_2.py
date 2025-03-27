#title:Random number file writer
#author: michael stoll
#date: 3/24/2025
import random
current_number = 0
total_numbers = int(input('How many numbers will be added to the file (up to 1000)?:'))
if total_numbers > 1000:
   total_numbers = 1000
with open("random_numbers.txt", "w") as f:
    f.write(str(random.randint(1, 500)))
    f.write('\n')
while current_number <= total_numbers - 2:
    with open("random_numbers.txt", "a") as f:
        f.write(str(random.randint(1, 500)))
        f.write('\n')
        current_number += 1