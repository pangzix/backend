from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserCreate,LoginView

app_name = 'userprofile'

urlpatterns = format_suffix_patterns({
    path('users/',UserCreate.as_view(),name=UserCreate.name),
    path('login/',LoginView.as_view(),name=LoginView.name),
})
