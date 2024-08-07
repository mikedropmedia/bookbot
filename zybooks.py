# Get the total number of ounces from the user
total_ounces = int(input("Enter the number of ounces: "))

# Calculate the number of tons
tons = total_ounces // (2000 * 16)

# Calculate the remaining ounces after converting to tons
remaining_ounces = total_ounces % (2000 * 16)

# Calculate the number of pounds from the remaining ounces
pounds = remaining_ounces // 16

# Calculate the remaining ounces after converting to pounds
remaining_ounces = remaining_ounces % 16

# Output the results
print(f'Tons: {tons}')
print(f'Pounds: {pounds}')
print(f'Ounces: {remaining_ounces}')
