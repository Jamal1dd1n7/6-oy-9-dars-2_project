from django.urls import path
# ----------------------------------------------------------------------------------------------------------------------------------------------------
from .views import *

urlpatterns = [
    # home 
    path('', home, name='home'),
    # ----------------------------------------------------------------------------------------------------------------------------------------------------
    
    # course
    path('type/<int:type_id>/', flower_by_type, name='flower_by_type'),
    path('type/add/', add_type, name='add_type'),
    path('type/<int:type_id>/', update_type, name='update_type'),
    path('type/<int:type_id>/', delete_type, name='delete_type'),
    # ----------------------------------------------------------------------------------------------------------------------------------------------------
    
    # lesson
    path('flower/<int:flower_id>/', flower_detail, name='flower_detail'),
    path('flower/add/', add_flower, name='add_flower'),
    path('flower/<int:flower_id>/', update_flower, name='update_flower'),
    path('flower/<int:flower_id>/', delete_flower, name='delete_flower'),
    # ----------------------------------------------------------------------------------------------------------------------------------------------------
   
    # comment
    path('flower/<int:flower_id>/comment/save/', comment_save, name='comment_save'),
    path('comment/<int:comment_id>/delete/', comment_delete, name='deleteComment'),
    path('comment/<int:comment_id>/update/', comment_update, name='updateComment'),
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 

    # auth
    path('auth/register/', register, name='register'),
    path('auth/login/', loginPage, name='login'),
    path('auth/logout/', logoutPage, name='logout'),
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
]