
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from article.views import home, detail
from about.views import about
from contact.views import contact



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('detail/<int:pk/', detail, name='detail')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings. MEDIA_ROOT)










