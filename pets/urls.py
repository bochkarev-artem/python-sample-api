# from django.urls import path
# from . import views
# from rest_framework_swagger.views import get_swagger_view
# from django.conf.urls import url
#
#
# app_name = 'pets'
# schema_view = get_swagger_view(title='Pets API')
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:pet_id>/detail/', views.detail, name='detail'),
#     path('<int:pet_id>/update/', views.update, name='update'),
#     url('docs/', schema_view),
# ]

from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from django.conf.urls import url, include
from rest_framework import routers
from pets.models import PetsViewSet


router = routers.DefaultRouter()
router.register(r'', PetsViewSet)


schema_view = get_schema_view(title='Pets API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [
    url(r'^docs/', schema_view, name="docs"),
    url(r'^', include(router.urls)),
]
