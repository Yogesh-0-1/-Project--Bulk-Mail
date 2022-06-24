
from django.contrib import admin
from django.urls import path
from MailSend  import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu_create/',views.StudentListCreate.as_view()),
    path('studentapi/<int:pk>/',views.student_RetrieveUpdateDestroy.as_view()),
    path('login', views.LogIn),

]
