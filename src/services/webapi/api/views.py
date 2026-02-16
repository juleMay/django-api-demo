from rest_framework.viewsets import ModelViewSet
from webapi.domain.models import Todo
from webapi.domain.serializers import TodoSerializer


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all().order_by("-created_at")
    serializer_class = TodoSerializer
