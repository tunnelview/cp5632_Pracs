COLOUR_NAME_TO_CODE = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7",
                       "antiquewhite4": "	#8b8378", "aquamarine1": "#7fffd4",
                       "aquamarine4": "#458b74", "azure1": "#f0ffff",
                       "azure4": "#838b8b", "black": "#000000",
                       "blue2": "#0000ee", "blueviolet": "#8a2be2", "brown4": "#8b2323"}

colour_name = input("Please enter your colour name: ")
while colour_name != "":
    if colour_name.lower() in COLOUR_NAME_TO_CODE:
        print(colour_name, "is", COLOUR_NAME_TO_CODE[colour_name.lower()])
    else:
        print("Invalid Colour Name!")
    colour_name = input("Please enter your colour name: ")

# Two ways- to look through all the keys - manual with case  insensitive matching
