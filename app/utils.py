from .models import Note


class NoteUtils:
    def __init__(self, model) -> None:
        self.model = model

    def get_note_object(self, note_id: int):
        return self.model.objects.get(pk=note_id)

    def get_user_notes(self, user_id: int):
        return self.model.objects.filter(author_id=user_id)

    def create_note(self, name: str, user):
        return self.model.objects.create(name=name, author=user)
    
    @staticmethod
    def delete_note(note: Note):
        return note.delete()
    

note_utils = NoteUtils(Note)
