import datetime

last_id = 0


class Note:
    """
    Class for representing note
    """
    def __init__(self, note, tag=''):
        self.note = note
        self.tag = tag
        self.creation_day = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        return filter in self.note or filter in self.tag


class Notebook:
    """
    Class for storing notes and working with them
    """
    def __init__(self):
        self.notes = []

    def new_note(self, note, tag=''):
        self.notes.append(Note(note, tag))

    def _find_note(self, note_id):
        """
        Locate the note with the given ID
        """
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_note(self, note_id, notes):
        """
        Locates note with given ID and modifies its note attribute
        """
        note = self._find_note(note_id)
        if note:
            note.note = notes
            return True
        return False

    def modify_tag(self, note_id, tag):
        """
        Locates note with given ID and modifies its tag attribute
        """
        self._find_note(note_id).tag = tag

    def search(self, filter):
        """
        Finds all notes with given filter
        """
        return [note for note in self.notes if note.match(filter)]


