from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from jobs.views import CompetencyViewSet, JobViewSet

router = routers.DefaultRouter()
router.register('jobs', JobViewSet)
router.register('competencies', CompetencyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
