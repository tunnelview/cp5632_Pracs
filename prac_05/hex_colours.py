COLOUR_CODE = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
               "AntiqueWhite4": "	#8b8378", "aquamarine1": "#7fffd4",
               "aquamarine4": "#458b74", "azure1": "#f0ffff",
               "azure4": "#838b8b", "black": "#000000",
               "blue2": "#0000ee", "BlueViolet": "#8a2be2", "brown4": "#8b2323"}

colour_name = input("Please enter your colour name: ")
while colour_name != "":
    if colour_name in COLOUR_CODE:
        print(colour_name, "is", COLOUR_CODE[colour_name])
    else:
        print("Invalid Colour Name!")
    colour_name = input("Please enter your colour name: ")



