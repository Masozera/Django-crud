# from django.contrib import admin  
from django.urls import path  
from . import views 
urlpatterns = [  
    # path('admin/', admin.site.urls),  
    path('homepage', views.homepage, name='homepage'),  
    path('show',views.show, name='show'),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update, name='update'),  
    path('delete/<int:id>', views.destroy),  
]  