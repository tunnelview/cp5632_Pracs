import wikipedia

page_title = input("Please enter the page title you want to search: ")
while page_title != "":
    print(wikipedia.search(page_title))
    print("----------------------------------------------------------------")

    print(wikipedia.summary(page_title))
    try:
        print(wikipedia.summary(page_title))
        search_page = wikipedia.page(page_title)
        print(search_page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print (e.options)
    # wikipedia.page(title, autosuggest=False) # autosuggest isn't available

    page_title = input("Please enter the page title you want to search: ")


""" (Note that didn't get a warning about an outdated use of the BeautifulSoup package.)"""









