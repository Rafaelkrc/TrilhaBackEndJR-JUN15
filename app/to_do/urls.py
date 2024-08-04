from django.urls import path
from app.to_do.views import ToDoCreateListView, ToDoRetrieveUpdateDestroyView


urlpatterns = [
    path('todo/', ToDoCreateListView.as_view(), name='todo_crate_list'),
    path('todo/<int:pk>/', ToDoRetrieveUpdateDestroyView.as_view(), name='todo_crate_list'),
]
