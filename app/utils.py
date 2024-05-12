from django.shortcuts import redirect

from .models import Note


class NoteUtils:
    def activate_note(self, post_data):
        note_id = post_data.get('activate_note')
        note_obj = self.__get_note_object(note_id)
        note_obj.is_active = True
        note_obj.save()

    def complete_note(self, post_data):
        note_id = post_data.get('complete_note')
        note_obj = self.__get_note_object(note_id)
        note_obj.is_active = False
        note_obj.save()

    def delete_note(self, note_id: int):
        note_obj = self.__get_note_object(note_id)
        note_obj.delete()

    @staticmethod
    def __get_note_object(note_id: int):
        return Note.objects.get(pk=note_id)

    @staticmethod
    def get_user_notes(user_id: int):
        return Note.objects.filter(author_id=user_id)

    # @staticmethod
    # def create_note(name: str, user):
    #     note = Note.objects.create(name=name, author=user)
    #     note.save()
    #     return redirect('app:home')


note_utils = NoteUtils()
