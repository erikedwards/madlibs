# Erik Edwards
# 10/8/2019
# Calculate supplies needed based on expected customers

OZ_PER_GAL = 128
OZ_PER_LB = 16

keep_on_truckin = True

while keep_on_truckin:
    # activate, initialize and calibrate as needed. This makes Francine think she's getting her money's worth
    print("\n\nCompruter activating...\n initializing \n  calibrating\n   calibration complete\n")
    print("wait... fuck, hold on\n re-calibrating...\n  re-calibrating...\n"
          "   diverting power from non-essential sub-systems...\n\nok, calibration complete\n")

    # down to business... how many folks are we expecting
    # remind Francine that strings are not numbers. "Twelve" gives a crash but "12" gives some fish facts
    customers = int(input("how many folks is this fish fry fixin to feed?\n"
                          "  (integers please, Francine... you didn't pay for error checking)\n"))
    print("\n-- compruting... \n\n")

    # Calculate ingredients needed for "x" customers based on Francine's experience:

    # The average customer orders 1.5 pieces of fish.
    # Each piece of fish is 4 ounces.
    fish_order_qty = 1.5 * customers
    fish_oz = fish_order_qty * 4

    # 75% of the orders include chips (fries).
    # An order of fries is 6 ounces of potatoes.
    chip_order_qty = 0.75 * customers
    chip_oz = chip_order_qty * 6

    # Each piece of fish is coated in 2.5 ounces of batter.
    batter_oz = fish_order_qty * 2.5

    # Each piece of fish is served with 1.2 ounces of tartar sauce.
    sauce_oz = fish_order_qty * 1.2

    # convert values from ounces to either gallons or pounds
    # tricky way to round up --> convert float to int to drop the digits, then +1 if there's a remainder (rad!)
    fish_lbs = int(fish_oz / OZ_PER_LB) + (fish_oz % OZ_PER_LB > 1)
    chip_lbs = int(chip_oz / OZ_PER_LB) + (chip_oz % OZ_PER_LB > 1)
    batter_gal = int(batter_oz / OZ_PER_GAL) + (batter_oz % OZ_PER_GAL > 1)
    sauce_gal = int(sauce_oz / OZ_PER_GAL) + (sauce_oz % OZ_PER_GAL > 1)

    print("FISH FACTS!!:\n\n"
          "Expected customers = " + str(customers) + " \n\n"
          # "Fish: " + str(fish_oz) + " oz\n"
          # "Chips: " + str(chip_oz) + " oz\n"
          # "Batter: " + str(batter_oz) + " oz\n"
          # "Sauce: " + str(sauce_oz) + " oz\n\n---but in lbs and gallons that would be....\n\n"
          "Fish: " + str(fish_lbs) + " lbs\n"
          "Chips: " + str(chip_lbs) + " lbs\n"
          "Batter: " + str(batter_gal) + " gals\n"
          "Sauce: " + str(sauce_gal) + " gals\n"
          "   and really some malt vinegar would be nice\n\n")


    # wrap it up
    if input("enter \"keep on truckin'!!\" to go again\n "
             "enter anything else to stop\n\n") != "keep on truckin'!!":
        keep_on_truckin = False