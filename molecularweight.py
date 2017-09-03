# molecularweight.py
#   Program to compute the molecular weight of a hydrocarbon
#   based on the number of hydrogen, carbon, and oxygen atoms.


H = 1.0079
C = 12.011
O = 15.9994

def main ():
    x, y, z = input("Please enter the number of Hydrogen, Carbon, and Oxygen atoms (Hyd, Carb, Oxy): ")

    molweight = (x * H) + (y * C) + (z * O)

    print
    print "The molecular weight of the hydrocarbon is: ", molweight

main()
