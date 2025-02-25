from fetcher import fetch_joke
from database_crud import *
from joke_response import add_metadata, search_jokes
from config import *

def menu():
    """CLI menu for interacting with the jokes database"""
    con = setup_connection(db_name)

    if con:
        # Create the table if not exists
        setup_database(db_name, con)

    while True:
        print("Welcome to Jokes Database Menu.")
        print("1) Fetch and store a new joke")
        print("2. View all jokes")
        print("3. Update a joke")
        print("4. Delete a joke")
        print("5. Search jokes")
        print("6. Exit")

        choice = input ("Choose an option: ")

        if choice == "1":
            num_jokes=int(input("How many jokes would you like to fetch? "))

            jokes = [fetch_joke() for _ in range(num_jokes)]

            if  jokes and all(jokes):
                print("\nHere are the jokes fetched from the API:\n")
                for index, joke in enumerate(jokes, 1):
                    print(f"{index})  {joke['setup']}\n    {joke['punchline']}\n")

                # Let user select which jokes to store
                selected_jokes = input("Enter the numbers of the jokes you want to store (comma-separated), or press 0 to go back to the main menu: ")
                selected_joke_ids = [int(id.strip()) for id in selected_jokes.split(',') if id.strip().isdigit()]

                # Establish DB connection
                con = setup_connection(db_name)

                for joke_id in selected_joke_ids:
                    if 1 <= joke_id <= len(jokes):  # Ensure valid selection
                        joke_to_store = jokes[joke_id - 1]  # Get joke by index
                        joke_to_store = add_metadata(joke_to_store)  # Add metadata
                        store_joke(joke_to_store, con)  # Store joke
                        print(f"Stored joke {joke_id} successfully!")
            else:
                print("Failed to fetch jokes.")

        elif choice == "2":
            jokes = get_jokes(con)
            if jokes:
                print("\nStored Jokes:")
                for joke in jokes:
                    joke_id, setup, punchline = joke  # Unpack tuple
                    print(f"ID: {joke_id} {setup} {punchline}")
            else:
                print("No jokes stored.")

        elif choice == "3":
            joke_id = int(input("Enter joke ID to update: "))
            new_punchline = input("Enter new punchline text: ")
            update_joke(joke_id, new_punchline, con)

        elif choice == "4":
            joke_id = int(input("Enter joke ID to delete: "))
            delete_joke(joke_id, con)

        elif choice == "5":
            keyword = input("Enter keyword to search for jokes: ")
            jokes = get_jokes(con)
            results = search_jokes(keyword, jokes)
            if results:
                for joke in results:
                    print(f"id: {joke[0]}, Setup: {joke[1]}, punchline: {joke[2]}")
            else:
                print("No jokes found")

        elif choice == "6":
            print("Goodbye")
            break

        else:
            print("Invalid choice, please select one of the options from the menu")

if __name__ == "__main__":
    menu()