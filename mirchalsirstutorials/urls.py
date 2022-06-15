from django.contrib import admin
from django.urls import path , include
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from django.conf import settings
from django.utils.html import format_html

admin.site.site_header  =  "Admin Panel - Mirchal Sir's Tutorials "  
admin.site.site_title  =  "Mirchal Sir's Tutorials"
admin.site.index_title  =  "Mirchal Sir's Tutorials"

handler404 = 'blog.views.custom_404'
handler500 = 'blog.views.custom_500'
urlpatterns = [
    path('admin/', admin.site.urls),
    path("" , include("courses.urls")),
    path('blog/', include('blog.urls')),
    path('quizzes/', include('quizapp.urls')),
    path('assignments/', include('assignments.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)