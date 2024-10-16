from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions
from api.viewsets.child.activity_viewset import ActivityModelViewset
from api.viewsets.child.allergies_viewset import AllergiesModelViewset
from api.viewsets.child.child_viewset import ChildModelViewset
from api.viewsets.child.specified_needs_viewset import SpecifiedNeedsModelViewset
from api.viewsets.parent.parent_viewset import ParentViewset
from api.viewsets.parent.user_role_viewset import UserRoleModelViewset
from api.viewsets.parent.user_viewset import UserModelViewset
from api.viewsets.plat.menu_viewset import MenuModelViewset
from api.viewsets.plat.personnel_viewset import PersonnelModelViewset
from api.viewsets.plat.plat_viewet import PlatModelViewset
from api.viewsets.plat.type_plat_viewset import TypePlatModoelViewset

router = routers.DefaultRouter()
router.register(r'parents', ParentViewset)
router.register('users', UserModelViewset)
router.register('childs', ChildModelViewset)
router.register('allergies', AllergiesModelViewset)
router.register('specifiedneeds', SpecifiedNeedsModelViewset)
router.register('activity', ActivityModelViewset)
router.register('plats', PlatModelViewset)
router.register('personnels', PersonnelModelViewset)
router.register('menus', MenuModelViewset)
router.register('typeplats', TypePlatModoelViewset)
router.register('userroles', UserRoleModelViewset)


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('', include(router.urls)),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]