import sys

from task_6 import Notebook, Note


class Menu:
    """
    Class for interacting with class Notebook
    """
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            '1': self.show_notes,
            '2': self.search_notes,
            '3': self.add_note,
            '4': self.modify_note,
            '5': self.quit
        }

    def display_menu(self):
        print("""
        Notebook Menu
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit
        """)

    def run(self):
        """
        Displays the menu and responds to choices
        """
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{} is not a valid choice".format(choice))

    def show_notes(self, notes=None):
        """
        Shows given notes
        """
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{}: {}\n{}".format(note.id, note.tag, note.note))

    def search_notes(self):
        """
        Searches for notes by given filter
        """
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        """
        Add note
        """
        note = input("Enter a note: ")
        self.notebook.new_note(note)
        print("Note has been added")

    def modify_note(self):
        """
        Searches note by given ID and modifies
        """
        id = input("Enter a note id: ")
        note = input("Enter a note: ")
        tag = input("Enter a tag: ")
        if note:
            self.notebook.modify_note(id, note)
        if tag:
            self.notebook.modify_tag(id, tag)

    def quit(self):
        print("Exit")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()

