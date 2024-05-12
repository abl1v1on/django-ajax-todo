from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .utils import note_utils
from .models import Note
from .forms import CreateNoteForm


@login_required
def index(request):
    if request.method == 'POST':
        post_data = request.POST

        # if post_data.get('complete_note'):
        #     note_utils.complete_note(post_data)
        #     return redirect('app:home')
        
        # elif post_data.get('activate_note'):
        #     note_utils.activate_note(post_data)
        #     return redirect('app:home')

        # elif post_data.get('delete-note'):
        #     note_utils.delete_note(post_data)
        #     return redirect('app:home')

    else:
        user_notes = note_utils.get_user_notes(request.user.id)

    context = {
        'title': 'Мои заметки',
        'notes': user_notes
    }
    return render(request, 'index.html', context=context)


# ПЕРЕПИСАТЬ НА ДРФ!!!
def delete_note_view(request):
    if request.method == 'POST':
        note_id = request.POST['note_id']
        note = Note.objects.get(pk=note_id)
        note.delete()
    return HttpResponse('Заметка успешно удалена')


def create_note(request):
    if request.method == 'POST':
        # name получим от имени ajax
        note_name = request.POST['name']

        note = Note.objects.create(name=note_name, author=request.user)
        note.save()
        return JsonResponse({
            'id': note.pk,
            'name': note.name,
            'date_created': note.date_create
        })


def complete_note_view(request):
    if request.method == 'POST':
        note_id = request.POST['note_id']
        note = Note.objects.get(pk=note_id)

        if note and note.is_active is True:
            note.is_active = False
            note.save()
        return JsonResponse({
            'id': note_id,
            'name': note.name,
            'date_create': note.date_create
        })
