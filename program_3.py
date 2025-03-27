#title:Average numbers
#author: michael stoll
#date: 3/27/2025
#I made this program use the same file as program_2 so they can work together
total_sum = 0
successful_line_count = 0
with open('random_numbers.txt', 'r') as f:
    for line in f:
        number = line.strip()
        try:
            integer = int(number)
            print(integer)
            total_sum += integer
            successful_line_count += 1
        except ValueError:
            print('NAN (not a number)')
try:
    print('The sum of every integer in the file:', total_sum * (successful_line_count/successful_line_count))
    #I added "* (successful_line_count/successful_line_count)"
    #to prevent this dialogue from printing when the file doesn't have any numbers
    #without otherwise changing the output
    print('The average of this sum is:', total_sum/successful_line_count)
except ZeroDivisionError:
    print('No numbers exist in this file')