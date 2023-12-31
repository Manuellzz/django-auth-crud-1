from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.signout, name="logout"),
    path("login/", views.signin, name="login"),
    path("password/change", views.change_password, name="change_password"),
    path("tasks/", views.tasks, name="tasks"),
    path("tasks/done", views.tasks_done, name="tasks_done"),
    path("tasks/create/", views.create_tasks, name="create_tasks"),
    path("tasks/<int:task_id>/", views.task_detail, name="task_detail"),
    path("tasks/<int:task_id>/complete/", views.complete_task, name="complete_task"),
    path("tasks/<int:task_id>/delete/", views.delete_task, name="delete_task"),
]
