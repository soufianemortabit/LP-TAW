from django.urls import path
from . import views

app_name = 'Afcon'
urlpatterns = [
    path('', views.index, name='index'),
    path('accueil.html', views.ViewAccueil, name='ViewAccueil'),
    path('groupe.html', views.ViewGroupe, name='ViewGroupe'),
    path('modifier/<int:equipe_id>/', views.ViewModifier, name='ViewModifier'),
    path('editPoints/<int:equipe_id>', views.editPoints, name='editPoints'),
    path('ViewMatches/<int:groupe_id>', views.ViewMatches, name='ViewMatches'),
    path('saveMatche', views.saveMatche, name='saveMatche'),
    path('huitieme.html', views.ViewHuitiemeFinal, name='ViewHuitiemeFinal'),
]