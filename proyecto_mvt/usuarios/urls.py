from django.urls import URLPattern, path
from . import views 


urlpatterns = [

    path("", views.inicio),
    path("lista_familiare" , views.lista_familiare),
    path("alta_familiare" , views.alta_familiare)

]