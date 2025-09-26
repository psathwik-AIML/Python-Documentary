def add_students():
    file = open("students.txt", "a")
    for i in range(3):
        name = input(f"Enter student name {i+1}: ")
        file.write(name + "\n")
    file.close()
    print("✅ Students added!")

def view_students():
    file = open("students.txt", "r")
    print("📃 All Students:")
    for line in file:
        print(line.strip())
    file.close()

def search_student():
    search_name = input("Enter name to search: ")
    found = False

    file = open("students.txt", "r")
    for line in file:
        if line.strip() == search_name:
            found = True
            break
    file.close()

    if found:
        print(f"✅ {search_name} is found in the list.")
    else:
        print(f"❌ {search_name} not found.")

# 💡 Menu to choose what you want
while True:
    print("\n--- Student Register ---")
    print("1. Add Students")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        add_students()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("👋 Exiting program. Bye!")
        break
    else:
        print("❌ Invalid choice.")
