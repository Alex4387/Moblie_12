#added
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), #a)
    path('', include('blog.urls')),
]

#added
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Post', views.IntruderImage)

urlpatterns = [
        path('', views.post_list, name='post_list’),
        path('api_root/', include(router.urls)),
    ]

from rest_framework.authtoken.views import obtain_auth_token #added

urlpatterns = [
    path('admin/', admin.site.urls), #a)
    path('', include('blog.urls')),
    path('api-token-auth/', obtain_auth_token), #added
]