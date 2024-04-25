import random
import nltk


# Import wikipedia module locally
import wikipedia as wiki

# Initialize NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Function to preprocess user input
def preprocess_input(user_input):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(user_input.lower())
    tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    return ' '.join(tokens)

# Function to fetch information from Wikipedia
def fetch_wikipedia_summary(query):
    try:
        return wiki.summary(query)
    except wiki.exceptions.DisambiguationError as e:
        return f"Multiple results found. Please specify your query. Here are some options: {', '.join(e.options)}"
    except wiki.exceptions.PageError:
        return "Sorry, I couldn't find information on that topic."

# Function to greet the user
def greet():
    responses = ["Hello! How can I assist you?", "Hi there! How can I help you today?", "Hey! What can I do for you?"]
    return random.choice(responses)

# Function to provide a response based on user input
def respond(user_input):
    preprocessed_input = preprocess_input(user_input)
    if "hello" in preprocessed_input or "hi" in preprocessed_input or "hey" in preprocessed_input:
        return greet()
    elif "how are you" in preprocessed_input:
        return "I'm just a computer program, but I'm here to help you!"
    elif "bye" in preprocessed_input or "goodbye" in preprocessed_input:
        return "Goodbye! Have a great day!"
    else:
        return fetch_wikipedia_summary(preprocessed_input)

# Main function to run the virtual assistant
def main():
    print("Welcome to the Intelligent Virtual Assistant!")
    print(greet())
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Virtual Assistant: Goodbye! Have a great day!")
            break
        else:
            response = respond(user_input)
            print("Virtual Assistant:", response)

if __name__ == "__main__":
    main()
