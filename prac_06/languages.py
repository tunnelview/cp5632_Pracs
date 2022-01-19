from prac_06.programming_language import ProgrammingLanguage

#list_of_languages = [] - This is not Java.

def main():
    #list_of_languages = [] - Place this variable here if it has a value and you adding on to it.


    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    list_of_languages = [ruby, python, visual_basic]

    print("The dynamically typed languages are:")
    for language in list_of_languages:
        if language.is_dynamic():
            print(language.field)


main()


