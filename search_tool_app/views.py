from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .serializers import (TypeSerializer, AuthorSerializer, YearSerializer,
                          TagSerializer, MaterialSerializer,
                          LanguageSerializer, PaperSerializer)
from rest_framework.response import Response
from .models import (Type, Language, Year, Tag, Material, Author, Paper,
                     )


''' start of class based views for rest_framework '''


class PagePagination(PageNumberPagination):
    # Set page size here
    page_size = 3

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

    def append_to_list(self, x):
        return list(map(int, self.request.GET.getlist(x)))

    def get_queryset(self):
        # A dictionary which gathers all the filters applied
        filters_dict = {}
        params = self.request.query_params

        # Adding to the Dictionary with the key:value pairs that Django can
        # use to filter objects

        if params.get('title'):
            filters_dict['title__icontains'] = params.__getitem__('title')

        if params.getlist('year[]'):
            filters_dict['year_id__in'] = self.append_to_list('year[]')

        if params.getlist('type[]'):
            filters_dict['type_id__in'] = self.append_to_list('type[]')

        if params.getlist('language[]'):
            filters_dict['language__in'] = self.append_to_list('language[]')

        if params.getlist('author[]'):
            filters_dict['author__in'] = self.append_to_list('author[]')

        if params.getlist('tag[]'):
            filters_dict['tag__in'] = self.append_to_list('tag[]')

        if params.getlist('material[]'):
            filters_dict['material__in'] = self.append_to_list('material[]')

        # If filter_dict is empty return all
        if filters_dict:
            results = list(Paper.objects.filter(**filters_dict).distinct())
            # the ** is unpacking a Dictionary, very cool
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
