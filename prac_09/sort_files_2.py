"""
Sort files based on extension and user categorisation
"""
import os


def main():
    extension_to_category = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]
        if extension not in extension_to_category:
            category = input("What category would you like to sort {} files into? ".format(extension))
            extension_to_category[extension] = category
            try:
                # We don't expect to get an exception due to the if statement
                # But we'll play it safe anyway in case the user chooses an existing folder
                os.mkdir(category)
            except FileExistsError:
                pass
        os.rename(filename, "{}/{}".format(extension_to_category[extension], filename))


main()
