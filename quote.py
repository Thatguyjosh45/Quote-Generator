import requests

def get_random_quote():
    url = "https://api.quotable.io/random"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        print(f"\"{data['content']}\" - {data['author']}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        print("\n=== Random Quote Generator ===")
        get_random_quote()
        again = input("\nWould you like another quote? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
