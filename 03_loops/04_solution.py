input_str = "Python"
reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str
print(f"Reverse of the string   '%s' is  '{reversed_str}'")

# # Another way to reverse a string using slicing technique.
# input_str = "Python"
# reversed_str = input_str[::-1]
# print(f"\nUsing Slicing Technique, Reverse of the string '%s' is  '{reversed_str}'")