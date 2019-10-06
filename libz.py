# mad libz
# 10-05-2019

#
# take me _(direction)_
# to the Paradise City
# where the _(noun)_ is _(color)_
# and the _(plural nouns)_ are _(adjective what rhymes with "City")_
#down

fun = True

while fun:
    direction = input("Enter a direction in which one could be taken")
    noun = input("Enter a noun")
    color = input("Enter a color")
    plural_noun = input("Enter a plural noun")
    adj_rhyme = input("Enter an adjective that rhymes with 'City', like maybe 'gritty' or 'shitty' or even 'witty'.")

    print("take me down {}\n"
          "to the paradise city\n"
          "where the grass {} is green {} \n"
          "and the girls {} are pretty {}\n"
          "OH WON'T YOU PLEASE\n"
          " TAKE ME HOME... WOH-OH-OH-AH".format(direction, noun, color, plural_noun, adj_rhyme))

    ans = input("again? (y/n)")
    if ans == "n":
        fun = False