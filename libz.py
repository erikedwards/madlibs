# mad libz
# 10-05-2019

#
# take me _(direction)_
# to the Paradise City
# where the _(noun)_ is _(color)_
# and the _(plural nouns)_ are _(adjective what rhymes with "City")_
# oh won't you please take me home. oh woh woh oh

fun = True

while fun:
    direction = input("Enter a direction in which one could be taken\n")
    noun = input("Enter a singular noun\n")
    color = input("Enter a color\n")
    plural_noun = input("Enter a plural noun\n")
    adj_rhyme = input("Enter an adjective that rhymes with 'City', like maybe 'gritty' or 'shitty' or even 'witty'.\n")

    print("\n"
          "\n"
          "\n"
          "take me {}\n"
          "to the paradise city\n"
          "where the {} is {} \n"
          "and the {} are {}\n"
          "OH WON'T YOU PLEASE\n"
          " TAKE ME HOME... WOH-OH-OH-AH\n"
          "\n"
          "".format(direction, noun, color, plural_noun, adj_rhyme))

    ans = input("again? (y/n)\n")
    if ans == "n":
        print("ok, importnat guy. Guy fuck off with your important stuff then, dick.")
        fun = False
