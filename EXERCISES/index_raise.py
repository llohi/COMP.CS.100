# COMP.CS.100 Indeksikorotus opintotukeen
# Tekijä: Joose Lohi
# Opiskelijanumero: 050800360

benefits = float(input("Enter the amount of the study benefits: "))
ind_raise = 1.0117
print("If the index raise is 1.17 percent, the study benefit,\nafter a raise, would be {0} euros\nand if there was another index raise, the study\nbenefits would be as much as {1} euros".format(
    benefits * ind_raise, benefits * ind_raise * ind_raise))
