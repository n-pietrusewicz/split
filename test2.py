from math import log
from os import system
from time import sleep

print("T")
sleep(2.2)
system('cls')
c1 = float(input("Person 1: How much are you going to save? $"))
c2 = float(input("Person 2: How much are you going to save? $"))
n = float(input("Goal (in months) to save? "))
int_rate = float(input("Annual interest rate (%)? "))

# FORMULAS (move into another file)
SAVING_RATE = (c1 + c2) * n
MONTHLY_INTEREST = int_rate / (12 * 100)
COMPOUNDING_INTEREST = (c1 + c2) * ((1 + MONTHLY_INTEREST)**n - 1) / MONTHLY_INTEREST
RS_BAL = log(1 + (COMPOUNDING_INTEREST * MONTHLY_INTEREST / (c1 + c2))) / log(1 + MONTHLY_INTEREST)
sleep(1)
system('cls')

print("\n")
print(f"""
        RESULTS:
        --------
        Person 1 savings (per month):\t${c1}
        Person 2 savings (per month):\t${c2}\n
        INTEREST:
        -------
        Yearly interest rate:\t{int_rate}%
        Which works out to\t{MONTHLY_INTEREST * 100:,.2f}% per month.\n

        In {n:,.0f} months, you will save:
        Without interest:\t${SAVING_RATE:,.2f}
        With interest:\t\t${COMPOUNDING_INTEREST:,.2f}
        Earned interest:\t${COMPOUNDING_INTEREST - SAVING_RATE:,.2f} in {n:,.0f} months.

      """)