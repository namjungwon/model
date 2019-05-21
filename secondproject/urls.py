from django.contrib import admin
from django.urls import path
import blog.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name = 'home'),
    path('write.html/', blog.views.write, name = 'write'),
    path('submit/', blog.views.submit, name="submit"),
]
