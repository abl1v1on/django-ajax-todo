from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required

from .utils import note_utils


@login_required
def index(request):
    user_notes = note_utils.get_user_notes(request.user.id)

    context = {
        'title': 'Мои заметки',
        'notes': user_notes
    }
    return render(request, 'index.html', context=context)


# ПЕРЕПИСАТЬ НА ДРФ!!!
@login_required
def delete_note_view(request):
    if request.method == 'POST':
        note_id = request.POST['note_id']
        note = note_utils.get_note_object(note_id)

        if note:
            note_utils.delete_note(note)
            return HttpResponse('Заметка успешно удалена')
        return JsonResponse({'detail': f'Заметка {note_id} не найдена :('})


@login_required
def create_note(request):
    if request.method == 'POST':
        note_name = request.POST['name']

        note = note_utils.create_note(name=note_name, user=request.user)
        note.save()
        return JsonResponse({
            'id': note.pk,
            'name': note.name,
            'date_created': note.date_create
        })


@login_required
def complete_note_view(request):
    if request.method == 'POST':
        note_id = request.POST['note_id']
        note = note_utils.get_note_object(note_id)

        if note and note.is_active is True:
            note.is_active = False
            note.save()
            return JsonResponse({
                'id': note_id,
                'name': note.name,
                'date_create': note.date_create
            })


@login_required
def activate_note(request):
    if request.method == 'POST':
        note_id = request.POST['note_id']
        note = note_utils.get_note_object(note_id)

        if note:
            note.is_active = True
            note.save()
            return JsonResponse({
                'id': note.pk,
                'name': note.name,
                'date_create': note.date_create
            })
