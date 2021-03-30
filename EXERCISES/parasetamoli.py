"""
COMP.CS.100 Parasetamoli
Tekijä: Joose Lohi
Opiskelijanumero: 050800360
"""


def calculate_dose(w, t, d):
    ''' CALCULATES THE MAX AMOUNT OF PARASETAMOL YOU CAN GIVE '''
    if t < 6 or d >= 4000:
        return 0
    else:
        if 4000 - (w * 15 + d) > 0:
            return w * 15
        else:
            return 4000 - d


def main():
    weight = int(input("Patient's weight (kg): "))
    time = int(input("How much time has passed from the previous dose (full hours): "))
    total_doze_24 = int(input("The total dose for the last 24 hours (mg): "))
    doze = calculate_dose(weight, time, total_doze_24)
    print("The amount of Parasetamol to give to the patient: {}".format(doze))


if __name__ == "__main__":
    main()
