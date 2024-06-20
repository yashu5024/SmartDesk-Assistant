from serpapi import GoogleSearch

def get_answer_from_google(query):
    params = {
        "engine": "google",
        "q": query,
        "api_key": "2f94ee311e3c6669a2c5a6035b7428dbb9c600abf0120f2582ae8f3063e08649"  # Replace with your actual API key
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    try:
        answer = results['answer_box']['snippet']
    except KeyError:
        answer = "Sorry, I couldn't find the answer to that question."
    return answer