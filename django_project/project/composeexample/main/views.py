from django.forms import models
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView
from main.models import Main
from django.views.generic.edit import DeleteView


class NoteDelete(DeleteView):
    model = Main
    template_name = 'main_confirm_delete.html'
    success_url = '/'


class NewNoteForm(models.ModelForm):
    class Meta:
        model = Main
        fields = ['text']


def new_note(request):
    if request.method == 'GET':
        form = NewNoteForm()
    else:
        form = NewNoteForm(request.POST)
        if form.is_valid():
            form.save()
            form = NewNoteForm()

    notes = Main.objects.filter(is_deleted=False)
    return render(request, 'main.html', {'notes': notes, 'form': form})


def main(request):
    notes = Main.objects.filter(is_deleted=False)
    form = NewNoteForm()
    return render(request, 'main.html', {'notes': notes, 'form': form})