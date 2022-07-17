from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),

    path('task/', views.TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task'),
    path('task-create/', views.TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', views.TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', views.DeleteView.as_view(), name='task-delete'),
    path('task-reorder/', views.TaskReorder.as_view(), name='task-reorder'),
    
    
    path('quiz/', views.QuizListView.as_view(), name='quiz-main-view'),
    path('quiz/<pk>/', views.quiz_view, name='quiz-view'),
    path('quiz/<pk>/save/', views.save_quiz_view, name='quiz-save-view'),
    path('quiz/<pk>/data/', views.quiz_data_view, name='quiz-data-view'),
    
    path('weather/', views.weather, name='weather'),
    path('delete/<city_name>/', views.delete_city, name='delete_city')
]