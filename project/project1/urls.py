from django.urls import path
from .views import home, flower_by_type, flower_detail, add_flower

urlpatterns = [
    path('', home, name='home'),
    path('type/<int:type_id>/', flower_by_type, name='flower_by_type'),
    path('flower/<int:flower_id>/', flower_detail, name='flower_detail'),
    path('flower/add/', add_flower, name='add_flower'),
]


