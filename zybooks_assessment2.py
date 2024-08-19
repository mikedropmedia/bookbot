
'''
Question 1
Instructions:
Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.

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
#Employee A: 15.62 miles
#Employee B: 41.85 miles
#Employee C: 32.67 miles
#solution accepts three integer inputs representing the number of times an employee travels to the job site
#solution outputs "Distance: " followed by the total value to two decimal places

trips_a = int(input())
trips_b = int(input())
trips_c = int(input())

# Define the distances for each employee
distance_a = 15.62
distance_b = 41.85
distance_c = 32.67

# Calculate the total distance for each employee
total_distance_a = trips_a * distance_a
total_distance_b = trips_b * distance_b
total_distance_c = trips_c * distance_c

# Calculate the total distance
total_distance = total_distance_a + total_distance_b + total_distance_c

# Output the total distance traveled
print(f"Distance: {total_distance:.2f} miles")

'''
Question 2
Instructions:
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
Question 3

Instructions:
Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.

Task:
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

# Get index value for element via user input
index_value = int(input())

# Access the element and determine type
element_type = type(various_data_types[index_value]).__name__

# Output the result
print(f"Element {index_value}: {element_type}")

#use built-in function type()
#get name by using the built-in attribute __name__
#solution accepts integer input representing list element index
#solution outputs data type of list element based on input index value

'''
Question 4
Instructions:
Adjust the existing Python code to run without errors and align to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.

Task:
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
'''

#solution accepts three integer values representing base and height measurements of a trapezoid
#first and second integers represent base 1 and base 2; third integer represents height
#solution outputs the trapezoid area in square meters using formula A = ½(b1+b2)h

input_base_1 = int(input())
input_base_2 = int(input())
input_height = int(input())

trap_area = (.5 * (input_base_1 + input_base_2)) * input_height
print(f'Trapezoid area: {trap_area} square meters')

'''
Question 5
Instructions:
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
# Step 1: Input the five integer values
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
Question 6
Instructions:
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
# Step 1: Input the 9-digit student identification number
student_id = input()

# Step 2: Convert to a string and format it
formatted_id = f"{student_id[:3]}-{student_id[3:5]}-{student_id[5:]}"

# Step 3: Output the formatted ID
print(formatted_id)

'''
Question 7
Instructions:
Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.

Task:
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
# Step 1: Input the 9-digit student identification number
student_id = input()

# Step 2: Convert to a string and format it
formatted_id = f"{student_id[:3]}-{student_id[3:5]}-{student_id[5:]}"

# Step 3: Output the formatted ID
print(formatted_id)

'''
Question 8
Instructions:
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
# Step 1: Input the water temperature
temperature = int(input())

# Step 2: Determine the water state and optional safety comment
if temperature < 33:
    water_state = "Frozen"
    safety_comment = "Watch out for ice!"
elif 33 <= temperature < 80:
    water_state = "Cold"
    safety_comment = ""
elif 80 <= temperature < 115:
    water_state = "Warm"
    safety_comment = ""
elif 115 <= temperature < 212:
    water_state = "Hot"
    safety_comment = ""
elif temperature >= 212:
    water_state = "Boiling"
    safety_comment = "Caution: Hot!" if temperature == 212 else ""

# Step 3: Output the results
print(water_state)
if safety_comment:
    print(safety_comment)
'''
Question 9
Instructions:
Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.

Task:
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

# Step 1: Define the list of frameworks
frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

# Step 2: Input the index value
try:
    index = int(input())

    # Step 3: Output the framework element based on the index
    print(frameworks[index])

# Step 4: Handle any exceptions (e.g., IndexError or ValueError)
except (IndexError, ValueError):
    print("Error")
'''
Question 10
Instructions:
Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.

Task:
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
'''
# Step 1: Define the dictionary with available stocks and their prices
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

# Step 2: Input the number of shares to be purchased
num_shares = int(input())

# Step 3: Initialize total cost
total_cost = 0.0

# Step 4: Loop to accept stock selections and calculate total cost
for i in range(num_shares):
    stock_selection = input()
    total_cost += stocks.get(stock_selection, 0)

# Step 5: Output the total cost formatted to two decimal places
print(f"Total price: ${total_cost:.2f}")

'''
Question 11
Instructions:
Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.

Task:
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
# Step 1: Define the dictionary with available items and their prices
purchase = {
    "bananas": 1.85,
    "steak": 19.99,
    "cookies": 4.52,
    "celery": 2.81,
    "milk": 4.34
}

# Step 2: Input the item and the number of items purchased
item = input()
quantity = int(input())

# Step 3: Look up the price per item
price_per_item = purchase.get(item, 0)

# Step 4: Calculate the total cost before discount
total_cost = price_per_item * quantity

# Step 5: Apply discount based on quantity
if 10 <= quantity <= 20:
    total_cost *= 0.95  # Apply 5% discount
elif quantity >= 21:
    total_cost *= 0.90  # Apply 10% discount

# Step 6: Output the result
print(f"{item} ${total_cost:.2f}")
'''
Question 12

Instructions:
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
# Step 1: Accept the filename as input
filename = input()

# Step 2: Open the file to read its contents
with open(filename, 'r') as file:
    words = file.read().splitlines()  # Read all lines and strip newline characters

# Step 3: Form the sentence from the words
sentence = ' '.join(words)

# Step 4: Open the file in append mode to add the new sentence
with open(filename, 'a') as file:
    file.write(f"\n{sentence}")

# Step 5: Reopen the file to read and print the new contents
with open(filename, 'r') as file:
    new_contents = file.read()
    print(new_contents)
'''
Question 13
Instructions:
Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.

Task:
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
# Step 1: Accept the name of the CSV file as input
filename = input()

# Step 2: Open and read the CSV file
with open(filename, 'r') as file:
    # Read the first row and split it into a list of values
    line1 = file.readline().strip().split(',')
    # Read the second row and split it into a list of values
    line2 = file.readline().strip().split(',')

# Step 3: Create dictionaries manually
dict1 = {}
for i in range(0, len(line1), 2):
    dict1[line1[i]] = line1[i+1]

dict2 = {}
for i in range(0, len(line2), 2):
    dict2[line2[i]] = line2[i+1]

# Step 4: Output the dictionaries
print(dict1)
print(dict2)
'''
Question 14
Instructions:
Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.

Task:
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

# Step 1: Accept an integer input
num = int(input())

# Step 2: Calculate the factorial using math.factorial()
factorial_value = math.factorial(num)

# Step 3: Determine if the factorial is greater than 100
is_greater_than_100 = factorial_value > 100

# Step 4: Output the results
print(factorial_value)
print(is_greater_than_100)
'''
Question 15
Instructions:
Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.

Task:
Create a solution that accepts an integer input representing the age of a pig. Import the existing module pigAge and use its pre-built pigAge_converter() function to calculate the human equivalent age of a pig. A year in a pig's life is equivalent to five years in a human's life. Output the human-equivalent age of the pig.

The solution output should be in the format

input_pig_age is converted_pig_age in human years
Sample Input/Output:
If the input is

8
then the expected output is

8 is 40 in human years
'''

import pigAge

def pigAge_converter(pig_age):
    return pig_age * 5

# Step 1: Accept an integer input representing the age of the pig
pig_age = int(input())

# Step 2: Use the pigAge_converter function to calculate human-equivalent age
human_age = pigAge_converter(pig_age)

# Step 3: Output the result in the specified format
print(f"{pig_age} is {human_age} in human years")
