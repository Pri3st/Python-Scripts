# Python script for decision making on cryptocurrency investments

#!/usr/bin/env python3

# User input
bc_inv=float(input("Insert your crypto investment."))
xrate=float(input("Insert the current exchange rate of your crypto to EUR."))
des=float(input("Insert your desired minimum investment return."))

# Calculate bitcoin to EUR
def bc2usd(bc_inv,xrate):
  usd_inv=bc_inv*xrate
  return usd_inv

inv=bc2usd(bc_inv, xrate)

# Decision
if inv<=des:
  print("DANGER")
else:
  print("ALL IS GOOD")