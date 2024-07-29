from django.contrib import admin
from django.urls import path
from .views import (
    login_view,
    logout_view,
    home_view,
    find_user_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('classify/', find_user_view, name='classify'),
]
