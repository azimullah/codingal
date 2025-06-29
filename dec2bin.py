# This script converts a decimal number to binary.
# It handles both integer and decimal parts.

number = input("Enter a decimal number: ")

if "." in number:
    int_part, dec_part = number.split(".")
    
    # Convert integer and decimal parts to binary
    binary_int = bin(int(int_part))[2:]
    binary_dec = bin(int(dec_part))[2:]  # Note: this is not a true binary fraction

    print("Binary int part:", binary_int + "." + binary_dec)
else:
    x = int(number)
    n = ""
    while x != 0:
        r = x % 2
        x = x // 2
        n = str(r) + n
        print(q, r)
    print(n)