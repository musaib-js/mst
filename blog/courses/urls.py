from django.contrib import admin
from django.urls import path , include
from courses import views
from courses.views import  MyCoursesList,  HomePageView,verifyPayment ,  coursePage , SignupView , LoginView , signout , checkout
from django.conf.urls.static import static
from django.conf import settings
from . import newviews

urlpatterns = [
    path('', HomePageView.as_view() , name = 'home'),
    path('about', newviews.about , name = 'about'),
    path('faqs', newviews.faqs , name = 'faqs'),
    path('teachers', newviews.teachers , name = 'teachers'),
    path('search', newviews.search, name="search"),
    path('profile', newviews.profile , name = 'profile'),
    path('contact', newviews.contact , name = 'contact'),
    path('logout', signout , name = 'logout'),
    path('allcourses', newviews.allcourses , name = "allcourses" ),
    path('my-courses', MyCoursesList.as_view() , name = 'my-courses'),
    path('signup', SignupView.as_view() , name = 'signup'),
    path('login', LoginView.as_view() , name = 'login'),
    path('course/<str:slug>', coursePage , name = 'coursepage'),
    path('check-out/<str:slug>', checkout , name = 'check-out'),
    path('verify_payment', verifyPayment , name = 'verify_payment'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)