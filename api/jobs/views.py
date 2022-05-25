from rest_framework import viewsets
from jobs.models import Competency, Job
from jobs.serializers import CompetencySerializer, JobSerializer


class CompetencyViewSet(viewsets.ModelViewSet):
    queryset = Competency.objects.all()
    serializer_class = CompetencySerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
