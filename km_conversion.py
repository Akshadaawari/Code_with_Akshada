#Assume a suitable value for distance between two cities(in km).
#write a program to convert and print this distance in meters ,feet,inches and centimeter
#KM_TO_INCHES = 39370.1
#KM_TO_FEET = 3280.84
kilometer=int(input("Enter the distance in kilometer :"))
kilometer_in_inches=39370.1*kilometer
kilometer_in_feet=3280.84*kilometer
kilometer_in_centimeter=100000*kilometer
kilometer_in_meter=1000*kilometer
print("The distance in inches",kilometer_in_inches)
print("the distance in feet",kilometer_in_feet)
print("the distance in centimeter",kilometer_in_centimeter)
print("the distance in meter",kilometer_in_meter)
