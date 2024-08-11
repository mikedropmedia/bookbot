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

# with open('info.txt', 'r') as file:
#     content = file.read
#     print(content)

# myList = [2000, 2004, 2008, 2012, 2016]

# def get_character_record(name, server, level, rank):
#     return {
#         "name": name,
#         "server": server,
#         "level": level,
#         "rank": rank,
#         "id": f"{name}#{server}",
#     }

# names = ["jack bronson", "jill mcarty", "john denver"]

# names_dict = {}
# for name in names:
#     # .split() returns a list of strings
#     # where each string is a single word from the original
#     name_list = name.split()

#     # here we update the dictionary
#     names_dict[name_list[0]] = name_list[1]

# print(names_dict)
# # Prints: {'jack': 'bronson', 'jill': 'mcarty', 'john': 'denver'}

# def count_enemies(enemy_names):
#     enemies_dict = {}
#     for enemy_name in enemy_names:
#         if enemy_name in enemies_dict:
#             enemies_dict[enemy_name] += 1
#         else:
#             enemies_dict[enemy_name] = 1
#     return enemies_dict

# fruit_sizes = {
#     "apple": "small",
#     "banana": "large",
#     "grape": "tiny"
# }

# for name in fruit_sizes:
#     size = fruit_sizes[name]
#     print(f"name: {name}, size: {size}")

# # name: apple, size: small
# # name: banana, size: large
# # name: grape, size: tiny

