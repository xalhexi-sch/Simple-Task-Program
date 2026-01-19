from app.manager import add_note, list_notes, read_note

def menu():
    print("\n=== Simple Notes Organizer ===")
    print("1) Add note")
    print("2) List notes")
    print("3) Read note")
    print("4) Exit")

def main():
    while True:
        menu()
        choice = input("Choose (1-4): ").strip()

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

        elif choice == "4":
            print("Bye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
