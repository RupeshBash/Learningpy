#note saver app

note= input("Enter your note: ")

#save the note to notes.txt(a there is append mode)
with open("notes.txt", "a") as file:
    file.write(note + "\n")

print("Note saved successfully!")

# Read and display all notes
print("Here is all notes so far:")
with open("notes.txt", "r") as file:
    notes = file.readlines()
    for index,line in enumerate(notes, start=1):
        print(f"{index}. {line.strip()}")