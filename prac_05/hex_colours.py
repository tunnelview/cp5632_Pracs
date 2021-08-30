COLOUR_CODE = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
               "AntiqueWhite4": "	#8b8378", "aquamarine1": "#7fffd4",
               "aquamarine4": "#458b74", "azure1": "#f0ffff",
               "azure4": "#838b8b", "black": "#000000",
               "blue2": "#0000ee", "BlueViolet": "#8a2be2", "brown4": "#8b2323"}

COLOUR_NAME = input("Please enter your colour name: ")
while COLOUR_NAME != "":
    if COLOUR_NAME in COLOUR_CODE:
        print(COLOUR_NAME, "is", COLOUR_CODE[COLOUR_NAME])
    else:
        print("Invalid Colur Name!")
    COLOUR_NAME = input("Please enter your colour name: ")



