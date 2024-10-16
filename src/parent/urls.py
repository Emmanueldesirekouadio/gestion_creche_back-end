from django.conf.urls.i18n import urlpatterns
from django.urls import path, include
from rest_framework import routers
from parent.viewsets.parent_viewset import ParentViewset


router = routers.DefaultRouter()
router.register(r'parents', ParentViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]