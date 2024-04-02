from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.parsers import FormParser
from rest_framework.permissions import IsAuthenticated

from .serializers import CategorySerializer, CategoryUpdateSerializer
from apps.foods.models import Category
from apps.common.permissions import IsAdmin, IsWaiter, IsClient


class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    parser_classes = (FormParser,)
    permission_classes = (IsAdmin | IsWaiter,)
    search_fields = ('name',)

    def get_permissions(self):
        if self.request.method == 'GET':
            return (IsAuthenticated(),)
        return (IsAdmin() or IsWaiter(),)


class CategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer
    parser_classes = (FormParser,)
    permission_classes = (IsAdmin | IsWaiter,)
    lookup_field = 'pk'
