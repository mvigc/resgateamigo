from django.conf import settings  # Adicione esta linha
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app.views import cadastrar_gato




urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastrar_gato/', cadastrar_gato, name='cadastrar_gato'),
    # Outras URLs do seu projeto
]


# Servir arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
