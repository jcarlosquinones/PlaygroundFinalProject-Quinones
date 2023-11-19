from django.urls import path
from AppCrud.views import *
from AppEntrega.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('grandespremios/', mostrarpistas, name="grandespremios"),
    path('registro/', Registro.as_view(), name="registro"),
    path('cerrarsesion/', cerrar_sesion, name="cerrar_sesion"),
    path('perfil/', PerfilView.as_view(), name="perfil"),
    # path('avatar/', AgregarAvatar, name="avatar"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)