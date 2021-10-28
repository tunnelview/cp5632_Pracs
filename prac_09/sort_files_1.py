import os


def main():
    """Move files into folders with the same name as their extension."""
    os.chdir("FilesToSort")  # chdir () to change the current working directory to specified path
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        print("{}/{}".format(extension, filename))
        os.rename(filename, "{}/{}".format(extension, filename))


main()
