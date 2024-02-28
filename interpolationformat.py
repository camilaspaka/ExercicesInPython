number_of_files = 3
numer_digits = int(input("How many digits are used in the numbering scheme? "))

for file_number in range(1, number_of_files + 1):
    print("image{number:0{padding_amount}.png".format(
        number=file_number,
        padding_amount=numer_digits
    ))