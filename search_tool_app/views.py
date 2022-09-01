from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .serializers import (TypeSerializer, AuthorSerializer, YearSerializer,
                          TagSerializer, MaterialSerializer,
                          LanguageSerializer, PaperSerializer)
from rest_framework.response import Response
from .models import (Type, Language, Year, Tag, Material, Author, Paper,
                     )

# new things for Vue in template
# imports for rest_framework


''' start of class based views for rest_framework '''


class PagePagination(PageNumberPagination):
    page_size = 2
    # Set page size here

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })


'''
CLASS BASED VIEWS
'''


class PaperViewSet(ModelViewSet):
    serializer_class = PaperSerializer
    # added for later on permissions of users etc.. 
    permission_classes = [AllowAny]
    pagination_class = PagePagination

    def get_queryset(self):
        # A dictionary which gathers all the filters applied
        filters_dict = {}

        # Adding to the Dictionary with the key:value pairs that Django can
        # use to filter objects
        if self.request.query_params.get('title'):
            filters_dict['title__icontains'] = self.request.query_params.get(
                'title')

        if self.request.query_params.get('year[]'):
            filters_dict['year_id__in'] = list(
                map(int, self.request.query_params.get('year[]')))

        if self.request.GET.getlist('type[]'):
            filters_dict['type_id__in'] = list(
                map(int, self.request.GET.getlist('type[]')))

        if self.request.query_params.get('langueage[]'):
            filters_dict['language__in'] = list(
                map(int, self.request.query_params.get('langueage[]')))

        if self.request.query_params.get('author[]'):
            filters_dict['author__in'] = list(
                map(int, self.request.query_params.get('author[]')))

        if self.request.GET.getlist('tag[]'):
            filters_dict['tag__in'] = list(
                map(int, self.request.GET.getlist('tag[]')))

        if self.request.query_params.get('material[]'):
            filters_dict['material__in'] = list(
                map(int, self.request.query_params.get('material[]')))

        # If filter_dict is empty return all
        if filters_dict:
            results = list(Paper.objects.filter(**filters_dict).distinct())
        else:
            results = Paper.objects.all().distinct()

        return results


class YearViewSet(ModelViewSet):
    serializer_class = YearSerializer
    queryset = Year.objects.all()


class TagViewSet(ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class TypeViewSet(ModelViewSet):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()


class LanguageViewSet(ModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


class MaterialViewSet(ModelViewSet):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
