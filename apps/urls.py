from django.urls import path

from apps.views import home_page, register_view, login_view, confirm

urlpatterns = [
    path('register/',register_view,name='register_view'),
    path('login/',login_view,name='login_view'),
    path('confirm/<uuid:id>',confirm,name='confirmation_code'),
    path('',home_page,name='home')
]