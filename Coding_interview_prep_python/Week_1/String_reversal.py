# Reversing a string manually
# original_string = "hello"
# reversed_string = ""
# for i in range(len(original_string) - 1, -1, -1):
#     reversed_string += original_string[i]

# print(reversed_string)  # Output: "olleh"

original_string = "salome"
reversed_string = ""

for i in range(1, len(original_string) + 1):
    # print(original_string[i], end = "")
    # print(f"index {i}, is {original_string[-i]}")
    reversed_string += original_string[-i]
print(reversed_string)