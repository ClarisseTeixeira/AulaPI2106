"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from formuario.views import cadastro_aluno, cadastro_professor
from projeto.views import cadastro_projeto
from matricula.views import criar_matricula

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro_aluno/', cadastro_aluno, name = "cadastro_aluno"),
    path('cadastro_projeto/', cadastro_projeto, name = "cadastro_projeto"),
    path('criar_matricula/', criar_matricula, name = "criar_matricula")
]
