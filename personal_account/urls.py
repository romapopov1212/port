from django.urls import path

from personal_account import views

app_name = 'personal_account'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.editProfile, name='edit_profile'),
    path('add_achievement/', views.addAchievement, name='add_achievement'),
]