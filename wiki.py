import wikipediaapi

def get_first_paragraph(input_term):
    user_agent = "wiki.py (ashwin080903@gmail.com)"  # Replace with your application's name and contact email
    wiki_wiki = wikipediaapi.Wikipedia('en', user_agent=user_agent)

    page_py = wiki_wiki.page(input_term)

    if page_py.exists():
        # Get the first paragraph
        first_paragraph = page_py.summary.split('\n')[0]
        
        print("Title:", page_py.title)
        print("First Paragraph:", first_paragraph)
    else:
        print("Page not found.")

# Example usage
input_term = "Python (programming language)"
get_first_paragraph(input_term)
