from django.contrib import admin
from django.urls import path
from Proyecto1.views import saludo # Para acceder a la vista hay que importar el modulo y el método

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', saludo),
    path('saludo/',saludo), #OJO. la url puede no llamarse "saludo/". el nombre es libre. La vista Si debe llamarse por su nombre
]
