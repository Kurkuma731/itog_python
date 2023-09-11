import json
import os
from datetime import datetime

notes_file = "notes.json"

if not os.path.exists(notes_file):
    with open(notes_file, "w") as file:
        json.dump([], file)

def add_note():
    title = input("Введите заголовок текста: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(notes_file, "r") as file:
        notes = json.load(file)
    new_note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }
    notes.append(new_note)
    with open(notes_file, "w") as file:
        json.dump(notes, file)
    print("Заметка успешно добавлена.")

def list_notes():
    with open(notes_file, "r") as file:
        notes = json.load(file)
    for note in notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Время создания: {note['timestamp']}")

def delete_note():
    id_to_delete = int(input("Введите ID заметки для удаления: "))
    with open(notes_file, "r") as file:
        notes = json.load(file)
    updated_notes = [note for note in notes if note["id"] != id_to_delete]
    with open(notes_file, "w") as file:
        json.dump(updated_notes, file)
    print(f"Заметка с ID {id_to_delete} удалена. ")

while True:
    print("\nМеню:")
    print("1. Добавить заметку")
    print("2. Список заметок")
    print("3. Удалить заметку")
    print("4. Выйти")
    choise = input("Выберите действие (1/2/3/4): ")
    if choise == "1":
        add_note()
    elif choise == "2":
        list_notes()
    elif choise == "3":
        delete_note()
    elif choise == "4":
        print("Выход из программы. ")
        break
    else:
        print("Неправильный выбор. Пожалуйста, выберите действие из меню.")