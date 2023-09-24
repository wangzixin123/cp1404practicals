import wikipedia

while True:
    search_input = input("Enter a page title or search phrase (blank to exit): ")

    if not search_input:
        break

    try:
        # Use autosuggest=False to prevent automatic page suggestion
        page = wikipedia.page(search_input, autosuggest=False)
        print("Title:", page.title)
        print("Summary:")
        print(page.summary)
        print("URL:", page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        # Handle disambiguation error
        print("Disambiguation Error: This search term is ambiguous. Please specify.")
    except wikipedia.exceptions.PageError as e:
        # Handle page not found error
        print("Page not found. Please try a different search term.")

print("Goodbye!")