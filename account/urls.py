from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from account import views

router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)

app_name = 'account'
urlpatterns = [
    url(r'^', include(router.urls))
]
