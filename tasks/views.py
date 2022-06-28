from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from .models import Task
from django.urls import reverse_lazy, reverse
from .forms import Todo
# Create your views here.


def index(request):
    form = Todo()

    if request.method == 'POST':
        form = Todo(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tasks')
    posts = Task.objects.all()
    remaining = len(posts)
    return render(request, 'index.html', {'form': form, 'posts': posts, 'remaining': remaining})


def delete(request, id):

    task = Task.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect(reverse('index'))
