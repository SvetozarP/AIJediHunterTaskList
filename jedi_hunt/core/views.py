from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .forms import TaskForm
from .models import Task
from .seed import ensure_tasks, VERBS
import random

from .utils import generate_task, random_planet, random_character, random_ship


# Create your views here.

def home(request):
    tasks = [generate_task() for _ in range(10)]
    return render(request, "core/home.html", {"tasks": tasks})

# ---------- main list ----------
def task_list(request):
    ensure_tasks()
    tasks = Task.objects.order_by('created_at')
    completed = tasks.filter(is_completed=True).count()
    total = tasks.count()
    percent = (completed / total) * 100 if total > 0 else 0

    return render(request, "core/task_list.html", {
        "tasks": tasks,
        "completed": completed,
        "total": total,
        "percent": percent,
    })

# ---------- toggle checkbox ----------
@require_POST
def toggle_task(request, pk):
    if request.method == "POST":
        task = get_object_or_404(Task, pk=pk)
        task.is_completed = not task.is_completed
        task.save()
    return redirect('task_list')


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'core/add_task.html', {'form': form})


@require_POST
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')


@require_POST
def add_random_task(request):
    """Create ONE new random task and return to list view."""
    Task.objects.create(
        planet_name=random_planet(),
        character_name=random_character(),
        ship_name=random_ship(),
        verb=random.choice(VERBS),
        is_completed=False,
    )
    return redirect("task_list")