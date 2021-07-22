from django.urls import path,include
from .views import Tasks
from rest_framework import routers

router=routers.DefaultRouter()
router.register('todo',Tasks,basename='api-data')


urlpatterns=[
    path('api/',include(router.urls))
]