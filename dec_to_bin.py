# decimal to binary conversion
# Erik Edwards
# 2019 10 12


fun = True

# get decimal value to convert
dec_val = int(input("Enter decimal value to convert\n\n"))

while fun:
    n = 0

    # find highest power of 2 that's still smaller than (or equal to) the decimal value
    # this is the number of digits in the binary value
    while 2**(n+1) <= dec_val:
        n = n + 1

    # start with blank string and add 1 or 0 for each digit to build binary value
    bin_val = ""

    # start from left (largest) digit and work down.
    # if 2^n fits, add a 1 and subtract 2^n from decimal value. If not, add a zero.
    # repeat with next smaller digit
    for i in range(n, -1, -1):
        if dec_val >= 2**i:
            bin_val = bin_val + "1"
            dec_val = dec_val - 2**i
        else:
            bin_val = bin_val + "0"

    print("= " + str(bin_val) + " in binary format\n")

    again = input("Again? Enter decimal value or 'x')\n")
    if str(again).lower() == "x":
        fun = False
    else:
        dec_val = int(again)
