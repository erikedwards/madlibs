# decimal to binary conversion
# Erik Edwards
# 2019 10 12


def main():
    fun = True
    while fun:
        inp_str = input("Enter decimal to convert or 'q' to quit\n")
        if str(inp_str).lower() == "q":
            fun = False
        else:
            b = dec_to_bin(int(inp_str))
            print(" = " + str(b) + " in binary format\n")


def dec_to_bin(dec_val):
    # find largest bin digit
    n = 0
    while 2**(n+1) <= dec_val:
        n = n + 1

    # fill bin string
    bin_val = ""
    for i in range(n, -1, -1):
        if dec_val >= 2 ** i:
            bin_val = bin_val + "1"
            dec_val = dec_val - 2**i
        else:
            bin_val = bin_val + "0"

    return bin_val


main()

