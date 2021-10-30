import wikipedia

page_title = input("Please enter the page title you want to search: ")
while page_title != "":
    print(wikipedia.search(page_title))
    print(wikipedia.summary(page_title))
    page_title = input("Please enter the page title you want to search: ")








