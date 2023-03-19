from django.contrib import admin
from django.urls import path
from todo_page import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="todo_page"),
    path('del/<str:item_id>', views.remove, name="del"),
    path('schedule/', views.schedule, name="schedule")
]
