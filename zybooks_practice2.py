'''
Task:
Create a solution that accepts three integer inputs representing the number of times an employee travels to a job site. Output the total distance traveled to two decimal places given the following miles per employee commute to the job site. Output the total distance traveled to two decimal places given the following miles per employee commute to the job site:

Employee A: 15.62 miles
Employee B: 41.85 miles
Employee C: 32.67 miles
The solution output should be in the format

Distance: total_miles_traveled miles
Sample Input/Output:
If the input is

1
2
3
then the expected output is

Distance: 197.33 miles
'''
# Define the miles per trip for each employee
miles_a = 15.62
miles_b = 41.85
miles_c = 32.67

# Prompt the user for the number of trips for each employee
trips_a = int(input("Enter the number of trips for Employee A: "))
trips_b = int(input("Enter the number of trips for Employee B: "))
trips_c = int(input("Enter the number of trips for Employee C: "))

# Calculate the total distance traveled by each employee
distance_a = trips_a * miles_a
distance_b = trips_b * miles_b
distance_c = trips_c * miles_c

# Calculate the overall total distance
total_distance = distance_a + distance_b + distance_c

# Format and display the total distance to two decimal places
print(f"Distance: {total_distance:.2f} miles")

# With a for loop:
# List of employees and their miles per trip
employees = {
    'A': 15.62,
    'B': 41.85,
    'C': 32.67
}

total_distance = 0.0

# Iterate over each employee to get trips and calculate distance
for emp, miles in employees.items():
    trips = int(input(f"Enter the number of trips for Employee {emp}: "))
    total_distance += trips * miles

# Display the total distance
print(f"Distance: {total_distance:.2f} miles")
'''
Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.

Task:
Create a solution that accepts an integer input representing any number of ounces. Output the converted total number of tons, pounds, and remaining ounces based on the input ounces value. There are 16 ounces in a pound and 2,000 pounds in a ton.

The solution output should be in the format

Tons: value_1
Pounds: value_2
Ounces: value_3
Sample Input/Output:
If the input is

32035
then the expected output is

Tons: 1
Pounds: 2
Ounces: 3
'''
#there are 16 ounces in a pound and 2000 pounds in a ton
#solution accepts an integer value representing any number of ounces
#solution outputs the converted tons, pounds, and ounces represented by the input value of ounces
# Input: number of ounces
ounces = int(input())

# Calculate the number of tons
tons = ounces // (2000 * 16)
# Calculate the remaining ounces after converting to tons
remaining_ounces = ounces % (2000 * 16)

# Calculate the number of pounds from the remaining ounces
pounds = remaining_ounces// 16
# Calculate the remaining ounces after converting to pounds
remaining_ounces = remaining_ounces % 16

# Output the result
print(f"Tons: {tons}")
print(f"Pounds: {pounds}")
print(f"Ounces: {remaining_ounces}")

'''
Create a solution that accepts an integer input representing the index value for any any of the five elements in the following list:

various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

Using the built-in function type() and getting its name by using the .name attribute, output data type (e.g., int”, “float”, “bool”, “str”) based on the input index value of the list element.

The solution output should be in the format

Element index_value: data_type
Sample Input/Output:
If the input is

4
then the expected output is

Element 4: tuple
'''
various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

#use built-in function type()
#get name by using the built-in attribute __name__
#solution accepts integer input representing list element index
#solution outputs data type of list element based on input index value
query_input = int(input())

data_type = type(various_data_types[query_input]).__name__

print(f'Element {query_input}: {data_type}')
'''
Create a solution that accepts any three integer inputs representing the base (b1, b2) and height (h) measurements of a trapezoid in meters. Output the exact area of the trapezoid in square meters as a float value. The exact area of a trapezoid can be calculated by finding the average of the two base measurements, then multiplying by the height measurement.

Trapezoid Area Formula:
A = [(b1 + b2) / 2] * h

The solution output should be in the format

Trapezoid area: area_value square meters
Sample Input/Output:
If the input is

3
4
5
then the expected output is

Trapezoid area: 17.5 square meters
Alternatively, if the input is

3
5
7
then the expected output is

Trapezoid area: 28.0 square meters
'''
base1 = int(input())
base2 = int(input())
height = int(input())
trap_area = (base1 + base2) / 2 * height
print(f'Trapezoid area: {trap_area} square meters')
'''
Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.

Task:
Create a solution that accepts five integer inputs. Output the sum of the five inputs three times, converting the inputs to the requested data type prior to finding the sum.

First output: sum of five inputs maintained as integer values
Second output: sum of five inputs converted to float values
Third output: sum of five inputs converted to string values (concatenate)
The solution output should be in the format

Integer: integer_sum_value
Float: float_sum_value
String: string_sum_value
Sample Input/Output:
If the input is

1
3
6
2
7
then the expected output is

Integer: 19
Float: 19.0
String: 13627
'''

inputs = []
for i in range(5):
    num = int(input())
    inputs.append(num)

# Step 2: Calculate the sum of the inputs as integers
integer_sum = sum(inputs)

# Step 3: Convert the sum to a float
float_sum = float(integer_sum)

# Step 4: Concatenate the inputs as strings
string_sum = ''.join(str(num) for num in inputs)

# Step 5: Output the results in the specified format
print(f"Integer: {integer_sum}")
print(f"Float: {float_sum}")
print(f"String: {string_sum}")

'''
Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.

Task:
Create a solution that accepts an integer input representing a 9-digit unformatted student identification number. Output the identification number as a string with no spaces.

The solution output should be in the format

111-22-3333
Sample Input/Output:
If the input is

154175430
then the expected output is

154-17-5430
'''
# Prompt the user for a 9-digit student identification number
student_id = input()

# Ensure the input has exactly 9 digits
if len(student_id) != 9 or not student_id.isdigit():
    print("Invalid input. Please enter a 9-digit number.")
else:
    # Slice the string into required parts
    part1 = student_id[:3]
    part2 = student_id[3:5]
    part3 = student_id[5:]

    # Format the ID with hyphens
    formatted_id = f"{part1}-{part2}-{part3}"

    # Display the formatted ID
    print(formatted_id)

# using modelo % and floored division //
# Prompt the user for a 9-digit student identification number
try:
    student_id = int(input())

    # Validate that the input is a 9-digit number
    if student_id < 100000000 or student_id > 999999999:
        print("Invalid input. Please enter a 9-digit number.")
    else:
        # Extract parts using floored division and modulo
        part1 = student_id // 1000000            # First three digits
        part2 = (student_id // 10000) % 100      # Middle two digits
        part3 = student_id % 10000                # Last four digits

        # Format each part with leading zeros if necessary
        formatted_id = f"{part1:03d}-{part2:02d}-{part3:04d}"

        # Display the formatted ID
        print(formatted_id)
except ValueError:
    print("Invalid input. Please enter a 9-digit integer.")


'''
Create a solution that accepts an integer input to compare against the following list:

predef_list = [4, -27, 15, 33, -10]

Output a Boolean value indicating whether the input value is greater than the maximum value from predef_list

The solution output should be in the format

Greater Than Max? Boolean_value
Sample Input/Output:
If the input is

20
then the expected output is

Greater Than Max? False
'''
predef_list = [4, -27, 15, 33, -10]

#solution accepts an integer input
#solution outputs Boolean value indicating if integer input is greater than the maximum value when compared to predef_list
comparison = int(input())
max_item = max(predef_list)

if comparison > max_item:
    print(f'Greater Than Max? {comparison > max_item}')

else:
    print(f'Greater Than Max? {comparison > max_item}')

# with error handling and cleaner:

# Define the predefined list
predef_list = [4, -27, 15, 33, -10]

# Prompt the user for an integer input
try:
    user_input = int(input())

    # Find the maximum value in predef_list
    max_value = max(predef_list)

    # Determine if the input is greater than the max value
    if user_input > max_value:
        is_greater = True
    else:
        is_greater = False

    # Display the result in the specified format
    print(f"Greater Than Max? {is_greater}")
except ValueError:
    # Handle cases where the input is not a valid integer
    print("Invalid input. Please enter an integer.")

'''
Create a solution that accepts one integer input representing the index value for any of the string elements in the following list:

frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

Output the string element of the index value entered. The solution should be placed in a try block and implement an exception of "Error" if an incompatible integer input is provided.

The solution output should be in the format

frameworks_element
Sample Input/Output:
If the integer input is

2
then the expected output is

CherryPy
Alternatively, if the integer input is

7
then the expected output is

Error
'''
frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

#use try block with exception "Error" when index value is not found in list
#solution accepts an integer input
#solution outputs the corresponding string value for the integer input

try:
    user_input = int(input())

    if frameworks[user_input] in frameworks:
        print(frameworks[user_input])

except:
    print('Error')

# also...

# Predefined list of frameworks
frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

try:
    # Prompt the user for an integer input (no prompt text to match output format)
    index = int(input())

    # Attempt to access the element at the provided index
    print(frameworks[index])
except (IndexError, ValueError):
    # If an IndexError (invalid index) or ValueError (invalid integer) occurs, print "Error"
    print("Error")
'''
Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.

Task:
Create a solution that accepts an integer input representing water temperature in degrees Fahrenheit. Output a description of the water state based on the following scale:

If the temperature is below 33° F, the water is “Frozen”.
If the water is between 33° F and 80° F (including 33), the water is “Cold”.
If the water is between 80° F and 115° F (including 80), the water is "Warm".
If the water is between 115° F and 211° (including 115) F, the water is “Hot".
If the water is greater than or equal to 212° F, the water is “Boiling”.
Additionally, output a safety comment only during the following circumstances:

If the water is exactly 212° F, the safety comment is "Caution: Hot!"
If the water temperature is less than 33° F, the safety comment is "Watch out for ice!"
The solution output should be in the format

water_state
optional_safety_comment
Sample Input/Output:
If the input is

118
then the expected output is

Hot
Alternatively, if the input is

32
then the expected output is

Frozen
Watch out for ice!
'''

# Read the temperature input as an integer
temperature = int(input())

# Determine the water state based on the temperature
if temperature < 33:
    water_state = "Frozen"
elif 33 <= temperature < 80:
    water_state = "Cold"
elif 80 <= temperature < 115:
    water_state = "Warm"
elif 115 <= temperature < 212:
    water_state = "Hot"
else:  # temperature >= 212
    water_state = "Boiling"

# Initialize safety_comment as an empty string
safety_comment = ""

# Determine if a safety comment is needed
if temperature == 212:
    safety_comment = "Caution: Hot!"
elif temperature < 33:
    safety_comment = "Watch out for ice!"

# Print the water state
print(water_state)

# If there is a safety comment, print it on the next line
if safety_comment:
    print(safety_comment)
"""
Create a solution that accepts an integer input identifying how many shares of stock are to be purchased from the Old Town Stock Exchange, followed by an equivalent number of string inputs representing the stock selections. The following dictionary stock lists available stock selections as the key with the cost per selection as the value.

stocks = {'TSLA': 912.86 , 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}

Output the total cost of the purchased shares of stock to two decimal places.

The solution output should be in the format

Total price: $cost_of_stocks
Sample Input/Output:
If the input is

3
SOFI
AMZN
LVLU
then the expected output is

Total price: $150.53
"""

# Predefined dictionary of stocks and their corresponding prices
stocks = {
    'TSLA': 912.86,
    'BBBY': 24.84,
    'AAPL': 174.26,
    'SOFI': 6.92,
    'KIRK': 8.72,
    'AURA': 22.12,
    'AMZN': 141.28,
    'EMBK': 12.29,
    'LVLU': 2.33
}

# Read the number of stock shares to purchase
try:
    num_shares = int(input())

    # Initialize total cost to zero
    total_cost = 0.0

    # Iterate over the number of shares to read each stock symbol
    for _ in range(num_shares):
        stock_symbol = input()

        # Retrieve the stock price from the dictionary
        if stock_symbol in stocks:
            total_cost += stocks[stock_symbol]
        else:
            # If the stock symbol is not found, you can choose to handle it accordingly
            # For this task, we'll assume all inputs are valid as per the sample
            pass

    # Format the total cost to two decimal places
    formatted_total = "{0:.2f}".format(total_cost)

    # Print the result in the specified format
    print(f"Total price: ${formatted_total}")

except ValueError:
    # Handle the case where the first input is not a valid integer
    print("Invalid input. Please enter a valid integer for the number of shares.")


'''
Create a solution that accepts a string input representing a grocery store item and an integer input identifying the number of items purchased on a recent visit. The following dictionary purchase lists available items as the key with the cost per item as the value.

purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

Additionally,

If fewer than ten items are purchased, the price is the full cost per item.
If between ten and twenty items (inclusive) are purchased, the purchase gets a 5% discount.
If twenty-one or more items are purchased, the purchase gets a 10% discount.
Output the chosen item and total cost of the purchase to two decimal places.

The solution output should be in the format

item_purchased $total_purchase_cost
Sample Input/Output:
If the input is

bananas
12
then the expected output is

bananas $21.09
Alternatively, if the input is

cookies
144
then the expected output is

cookies $585.79
'''

# Define the purchase dictionary with items and their prices
purchase = {
    "bananas": 1.85,
    "steak": 19.99,
    "cookies": 4.52,
    "celery": 2.81,
    "milk": 4.34
}

# Read the item name from user input
item = input()

# Read the quantity as an integer from user input
quantity = int(input())

# Retrieve the price per item from the dictionary
price_per_item = purchase[item]

# Calculate the initial total cost
initial_total = price_per_item * quantity

# Determine the discount rate based on quantity
if quantity < 10:
    discount_rate = 0.0  # No discount
elif 10 <= quantity <= 20:
    discount_rate = 0.05  # 5% discount
else:
    discount_rate = 0.10  # 10% discount

# Calculate the final total cost after applying discount
total_cost = initial_total * (1 - discount_rate)

# Format the total cost to two decimal places
formatted_total = "{0:.2f}".format(total_cost)

# Print the result in the specified format
print(f"{item} ${formatted_total}")

'''
Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.

Task:
Create a solution that accepts an input identifying the name of a text file, for example, "WordTextFile1.txt". Each text file contains three rows with one word per row. Using the open() function and write() and read() methods, interact with the input text file to write a new sentence string composed of the three existing words to the end of the file contents on a new line. Output the new file contents.

The solution output should be in the format

word1
word2
word3
sentence
Sample Input/Output:
If the input is

WordTextFile1.txt
then the expected output is

cat
chases
dog
cat chases dog
'''

# Step 1: Read the file name from user input
file_name = input()

# Step 2: Open the file in read mode and read the existing words
with open(file_name, 'r') as file:
    lines = file.readlines()

# Strip newline characters and extract words
word1 = lines[0].strip()
word2 = lines[1].strip()
word3 = lines[2].strip()

# Step 3: Create the sentence by concatenating the three words
sentence = f"{word1} {word2} {word3}"

# Step 4: Open the file in append mode and write the sentence
with open(file_name, 'a') as file:
    file.write(f"\n{sentence}")

# Step 5: Open the file in read mode again to read all contents
with open(file_name, 'r') as file:
    updated_lines = file.readlines()

# Print each line without additional spaces or newlines
for line in updated_lines:
    print(line.strip())
'''
Create a solution that accepts an input identifying the name of a CSV file, for example, "input1.csv". Each file contains two rows of comma-separated values. Import the built-in module csv and use its open() function and reader() method to create a dictionary of key:value pairs for each row of comma-separated values in the specified file. Output the file contents as two dictionaries.

The solution output should be in the format

{'key': 'value', 'key': 'value', 'key': 'value'}
{'key': 'value', 'key': 'value', 'key': 'value'}
Sample Input/Output:
If the input is

input1.csv
then the expected output is

{'a': '100', 'b': '200', 'c': '300'}
{'bananas': '1.85', 'steak': '19.99', 'cookies': '4.52'}
Alternatively, if the input is

input2.csv
then the expected output is

{'d': '400', 'e': '500', 'f': '600'}
{'celery': '2.81', 'milk': '4.34', 'bread': '5.63'}
'''

import csv

# Step 1: Read the CSV file name from user input
file_name = input()

# Initialize a list to hold the dictionaries
dict_list = []

# Step 2: Open the CSV file and read its contents
try:
    with open(file_name, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)

        # Iterate over each row in the CSV
        for row in csv_reader:
            # Initialize an empty dictionary for the current row
            current_dict = {}

            # Iterate over the row in steps of 2 to get key-value pairs
            for i in range(0, len(row), 2):
                key = row[i].strip()
                value = row[i+1].strip()
                current_dict[key] = value

            # Append the current dictionary to the list
            dict_list.append(current_dict)

    # Step 3: Print each dictionary in the specified format
    for dictionary in dict_list:
        print(dictionary)

except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
except IndexError:
    print("Error: The CSV file does not contain an even number of elements in a row.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
'''
Create a solution that accepts an integer input. Import the built-in module math and use its factorial() method to calculate the factorial of the integer input. Output the value of the factorial, as well as a Boolean value identifying whether the factorial output is greater than 100.

The solution output should be in the format

factorial_value
Boolean_value
Sample Input/Output:
If the input is

10
then the expected output is

3628800
True
Alternatively, if the input is

3
then the expected output is

6
False
'''
import math

try:
    n = int(input())
    fact = math.factorial(n)
    is_greater = fact > 100
    print(fact)
    print(is_greater)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except OverflowError:
    print("The number is too large to compute its factorial.")
'''
Create a solution that accepts an integer input representing the age of a pig. Import the existing module pigAge and use its pre-built pigAge_converter() function to calculate the human equivalent age of a pig. A year in a pig's life is equivalent to five years in a human's life. Output the human-equivalent age of the pig.

The solution output should be in the format

input_pig_age is converted_pig_age in human years
Sample Input/Output:
If the input is

8
then the expected output is

8 is 40 in human years
'''

# Step 1: Import the pigAge module
import pigAge

# Step 2: Read the pig's age as an integer from user input
pig_age_input = int(input())

# Step 3: Calculate the human-equivalent age using pigAge_converter()
human_equivalent_age = pigAge.pigAge_converter(pig_age_input)

# Step 4: Print the result in the specified format
print(f"{pig_age_input} is {human_equivalent_age} in human years")



