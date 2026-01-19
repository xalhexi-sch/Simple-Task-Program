from app.manager import add_note, list_notes, read_note, delete_note  # <- added delete_note

def menu():
    print("\n=== Simple Notes Organizer ===")
    print("1) Add note")
    print("2) List notes")
    print("3) Read note")
    print("4) Delete note")   # <- new menu option
    print("5) Exit")          # <- shifted exit to 5

def main():
    while True:
        menu()
        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            title = input("Title: ").strip()
            content = input("Content: ").strip()
            add_note(title, content)
            print("✅ Note saved!")

        elif choice == "2":
            notes = list_notes()
            if not notes:
                print("No notes yet.")
            else:
                print("\nSaved notes:")
                for i, n in enumerate(notes, 1):
                    print(f"{i}. {n}")

        elif choice == "3":
            title = input("Enter note title to read: ").strip()
            text = read_note(title)
            if text is None:
                print("❌ Note not found.")
            else:
                print("\n--- Note ---")
                print(text)

        elif choice == "4":  # <- new delete note
            title = input("Enter note title to delete: ").strip()
            if delete_note(title):
                print("✅ Note deleted!")
            else:
                print("❌ Note not found.")

        elif choice == "5":   # <- exit updated
            print("Bye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
