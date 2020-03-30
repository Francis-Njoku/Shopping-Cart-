"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls//
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from userlog.views import classroom, students, teachers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('home/', classroom.home, name='home'),
    path('backend/', include('django.contrib.auth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('shop.urls')), 
    #path('chrome/quiz/<int:pk>/', teachers.QuizUpdateView.as_view(), name='quiz_change'),
    path('teachers/list', teachers.QuizListView.as_view(), name='teachers_view'),
    path('home/', include('userlog.urls')),
    #path('chrome/', include('userlog.urls')),
    path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
