import wikipedia

search_page_title = input("Please enter the page title you want to search: ")
while search_page_title != "":
    print(wikipedia.search(search_page_title))
    print(wikipedia.summary(search_page_title))
    search_page_title = input("Please enter the page title you want to search: ")








