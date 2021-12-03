"""islam_test_avdev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from employee.views import EmployersList, EmployersCreateView, EmployersUpdateView, EmployersDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employers_list/', EmployersList.as_view(), name='employers'),
    path('employer_add/', EmployersCreateView.as_view(), name='employer_add'),
    path('employer_add/<int:pk>/', EmployersUpdateView.as_view(), name='employer_update'),
    path('employer_delete/<int:pk>/', EmployersDeleteView.as_view(), name='employer_delete'),

]
