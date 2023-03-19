from django.shortcuts import render, redirect
from django.contrib import messages
import requests
from django.http import HttpResponse

from .forms import TodoForm
from .models import Todo


def index(request):
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_page')
    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "Ежедневник",
    }
    return render(request, 'todo_page/index.html', page)


def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "Заметка удалена")
    return redirect('todo_page')


def schedule(request):
    current_week = requests.get("https://mirea.xyz/api/v1.3/time/week").json()
    url = requests.get(f'https://mirea.xyz/api/v1.3/groups/certain?name=%D0%91%D0%A1%D0%9C%D0%9E-01-22')
    data = url.json()
    if current_week % 2:
        week_val = "odd"
    else:
        week_val = "even"
    response = f"<h2>Сейчас идет {current_week} неделя</h2><br>"
    for day in data[0]["schedule"]:
        response += f"<h3><b>{day['day']}</b></h3><br>"
        for i in range(len(day[week_val])):
            exception = ""
            if day[week_val][i]:
                if day[week_val][i][0]['weeks']:
                    exception = day[week_val][i][0]['weeks']
                response += f"{i + 1} пара {exception} - {day[week_val][i][0]['name']} - {day[week_val][i][0]['place']} - {day[week_val][i][0]['type']}<br>"
    return render(request, 'todo_page/schedule.html', {"response": response})
