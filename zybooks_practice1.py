# Get the total number of ounces from the user
# total_ounces = int(input("Enter the number of ounces: "))

# Calculate the number of tons
# tons = total_ounces // (2000 * 16)

# Calculate the remaining ounces after converting to tons
# remaining_ounces = total_ounces % (2000 * 16)

# Calculate the number of pounds from the remaining ounces
# pounds = remaining_ounces // 16

# Calculate the remaining ounces after converting to pounds
# remaining_ounces = remaining_ounces % 16

# Output the results
# print(f'Tons: {tons}')
# print(f'Pounds: {pounds}')
# print(f'Ounces: {remaining_ounces}')

# file read and write practice:
# with open('info.txt', 'w') as file:
#     file.write('Name: John Doe\n')
#     file.write('Age: 30\n')
#     file.write('Hobby: Reading\n')
#   file.write('Name: John Doe\n')
#   file.write('Age: 30\n')
#   file.write('Hobby: Reading\n')

# Reading from the file
# with open('info.txt', 'r') as file:
#   content = file.read()
#   print(content)

# with open('info.txt', 'w') as file:
#   file.write('Name: Mike Dawg\n')
#   file.write('Age: 42\n')
#   file.write('Hobby: MTB\n')

# with open('info.txt', 'r') as file:
#   content = file.read()
#   print(content)

with open('info.txt', 'r') as file:
    content = file.read
    print(content)
    