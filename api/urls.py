from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter
from api import views

# router = SimpleRouter(trailing_slash=False)

app_name = 'api'
urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^account/', include('account.urls', namespace='account'))
]
