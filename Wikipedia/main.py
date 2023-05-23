import wikipedia

# search_results = wikipedia.search("Python programming")
# print(search_results)

page = wikipedia.page("List of Python software")
print(page.summary)