import sys
import os
from decimal import Decimal
Entry = Decimal(input("Entry: "))
Target = Decimal(input("Target: "))
SL = Decimal(input("Stop Loss: "))

os.system("clear")

RR = (Target - Entry)/(Entry - SL)
RR = round(RR, 2)
print (f"Your Risk Ratio is: {RR}")

sys.exit()
