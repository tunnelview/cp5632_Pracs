"""
Cleanup inconsistent song lyrics file names
Note: A complete solution for this exercise is NOT provided.
It's a very good thinking exercise and is less about the patterns we usually focus on
and more of a "tricky" problem to solve.
"""
import os


def main():

    """Cleanup inconsistent song lyrics file names."""

    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))

            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            os.rename(full_name, new_name)
            get_fixed_filename(new_name)


def get_fixed_filename(filename):
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name = ""
    for word, char in enumerate(filename):
        try:
            if filename[word + 1].isupper():
                new_name = new_name + f"{char}_"
            else:
                new_name += char
        except IndexError:
            new_name += char
    return new_name


main()

