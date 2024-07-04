


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cliente_transfer/<int:ticket>', views.qr_cliente, name='cliente_transfer'),
    # chofer_dashboard
    path('register/chofer/', views.chofer_register, name='chofer_register'),
    path('chofer/dashboard/', views.chofer_dashboard, name='chofer_dashboard'),
    
    path('logout', views.logout, name='logout'),


    # crud
    path('finalizarTick/<int:id>/', views.finalizar, name="finalizarTick"),
     path('deleteTick/<int:id>/', views.delete, name="deleteTick"),
]