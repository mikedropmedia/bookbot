# Tracks frequency of domains in web searches
import web_search

domains = {}

terms = input("Enter search terms ('q' to quit): ")
while terms != 'q':
    results = web_search.search(terms)

    # ...

print('\nNumber of search results for each site:')
for domain, num in domains.items():
    print(domain + ':', num  )