from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from casemgr.views import rest

router = routers.DefaultRouter()


# casemgr API Endpoints
# router.register(r"model_name", rest.ModelViewSet, "model_name")


urlpatterns = [
    # API views
    path("rest/", include(router.urls)),
]
