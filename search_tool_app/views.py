from turtle import title
from unittest import result
from urllib import request
from django.shortcuts import render
from .forms import PaperForm, SearchForm, MaterialUsedForm
from .models import *
from functools import reduce
from django.db.models import Q
from django.urls import reverse
# new things for Vue in template
import json
import random
# for objects to serialise to json

from django.core import serializers
# imports for rest_framework

from rest_framework.response import Response
from rest_framework import generics
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

''' start of class based views for rest_framework '''

'''
CLASS BASED VIEWS 
'''
class PaperViewSet(ModelViewSet):
    serializer_class = PaperSerializer
    permission_classes = [AllowAny]
    #added for later on permissions of users etc.. not a bad idea to define

    def get_queryset(self):
        filters_dict = {}
        mat_filters_dict = {}

        title_param = self.request.query_params.get('title')
        # print(self.request.GET.getlist('tag[]'))
        # print(self.request.GET.getlist('author[]'))

        if self.request.query_params.get('title'):
            print("title query == "+ self.request.query_params.get('title'))
            filters_dict['title__icontains'] = self.request.query_params.get('title')

        # import ipdb; ipdb.set_trace()


        # if self.request.GET.getlist('tag[]'):
        #     # print("tag query == "+ self.request.GET.getlist('tag[]'))
        #     print(self.request.GET.getlist('tag[]'))
        #     filters_dict['tag__tag'] = self.request.GET.getlist('tag[]')

# edw kapou paizei h malakia, psaxnei lathos rpagmata se lathos pedia 
     

        # if title_filter:
        #     filters_dict['title__icontains'] = title_filter
        #     mat_filters_dict['paper__title__icontains'] = title_filter
        # if year_filter:
        #     filters_dict['year_id__in'] = year_filter
        #     mat_filters_dict['paper__year_id__in'] = year_filter
        # if type_filter:
        #     filters_dict['type_id__in'] = type_filter
        #     mat_filters_dict['paper__type_id__in'] = type_filter
        # if lang_filter:
        #     filters_dict['language__in'] = lang_filter
        #     mat_filters_dict['paper__language__in'] = lang_filter
        # if tag_filter:
        #     filters_dict['tag__in'] = tag_filter
        #     mat_filters_dict['paper__tag__in'] = tag_filter
        # if material_filter:
        #     filters_dict['material__in'] = material_filter
        #     mat_filters_dict['paper__material__in'] = material_filter

        # # this is not the best way to do this. SQLite though doesn't support `DISTINCT`
        # # Fix this when we change to PostgreSQL
        results = set(Paper.objects.filter(**filters_dict))
        # papers_materials = PaperUsedMaterial.objects.filter(paper_id__in=[p.id for p in results])

        # print('title parameter ', title_param)
        # results = {}

        
        return results


class YearViewSet(ModelViewSet):
    serializer_class = YearSerializer
    queryset = Year.objects.all()
# na ginoun ola ModelViewSet?? anti gia generics.RetrieveAPIView ..nomizw kalutera gia pio polla options 

class YearView(generics.RetrieveAPIView):
    queryset = Year.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = YearSerializer(queryset, many=True)
        return Response(serializer.data)


class TagView(generics.RetrieveAPIView):
    queryset = Tag.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = TagSerializer(queryset, many=True)
        return Response(serializer.data)


class AuthorView(generics.RetrieveAPIView):
    queryset = Author.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)


class TypeView(generics.RetrieveAPIView):
    queryset = Type.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = TypeSerializer(queryset, many=True)
        return Response(serializer.data)


class LanguageView(generics.RetrieveAPIView):
    queryset = Language.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = LanguageSerializer(queryset, many=True)
        return Response(serializer.data)


class MaterialView(generics.RetrieveAPIView):
    queryset = Material.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = MaterialSerializer(queryset, many=True)
        return Response(serializer.data)

        
# class PaperView(ModelViewSet):
#     queryset = Paper.objects.all()
#     template_name = "../templates/search_tool_app/vue_search.html"
#
#     serializer_class = PaperSerializer
#     # def get(self, request, *args, **kwargs):
#
#     #     return Response(serializer.data)

''' FUNCTION BASED VIEWS '''
def homepage(request):
    context_dict = {}

    return render(request, 'search_tool_app/homepage.html', context=context_dict)


def post_a_publication(request):
    form = PaperForm()
    matform = MaterialUsedForm()
    if request.method == 'POST':
        # for i, k in request.POST.lists():
        #     for j in k:
        #         print()

        form = PaperForm(request.POST, request.FILES)
        # import ipdb;
        # ipdb.set_trace()

        if form.is_valid():
            pap = form.save(commit=True)
            pap.save()
            print('Paper ', pap, "has been registered")  # here only as a confirmation on the terminal
            return homepage(request)
        else:
            print(form.errors)
    return render(request, 'search_tool_app/post_a_publication.html', context={'form': form,
                                                                               'matform': matform})


def search_publication(request):
    form = SearchForm()
    if request.method == 'GET':
        # Provide the initial data required to render the search options

        return render(request, 'search_tool_app/search_publication.html',
                      context={'form': form}
                      )
    elif request.method == 'POST':

        form = SearchForm(request.POST)

        if form.is_valid():
            title_filter = form.cleaned_data['title']
            year_filter = list(form.cleaned_data['year'].values_list('id', flat=True))
            type_filter = list(form.cleaned_data['type'].values_list('id', flat=True))
            lang_filter = list(form.cleaned_data['language'].values_list('id', flat=True))
            tag_filter = list(form.cleaned_data['tag'].values_list('id', flat=True))
            material_filter = list(form.cleaned_data['material'].values_list('id', flat=True))
            filters_dict = {}
            mat_filters_dict = {}

            if title_filter:
                filters_dict['title__icontains'] = title_filter
                mat_filters_dict['paper__title__icontains'] = title_filter
            if year_filter:
                filters_dict['year_id__in'] = year_filter
                mat_filters_dict['paper__year_id__in'] = year_filter
            if type_filter:
                filters_dict['type_id__in'] = type_filter
                mat_filters_dict['paper__type_id__in'] = type_filter
            if lang_filter:
                filters_dict['language__in'] = lang_filter
                mat_filters_dict['paper__language__in'] = lang_filter
            if tag_filter:
                filters_dict['tag__in'] = tag_filter
                mat_filters_dict['paper__tag__in'] = tag_filter
            if material_filter:
                filters_dict['material__in'] = material_filter
                mat_filters_dict['paper__material__in'] = material_filter

            # this is not the best way to do this. SQLite though doesn't support `DISTINCT`
            # Fix this when we change to PostgreSQL
            results = set(Paper.objects.filter(**filters_dict))
            papers_materials = PaperUsedMaterial.objects.filter(paper_id__in=[p.id for p in results])

            return render(request, 'search_tool_app/search_publication.html', {
                'results': results,
                'papers_materials': papers_materials,
                'form': form
            })
        else:
            return "form is not valid"

    return render(request, 'search_tool_app/search_publication.html', {
        'form': form
    })


# papers = Paper.objects.filter(reduce(lambda x, y: x | y, [Q(type_id__type__icontains=word) for word in
#                                                  form.cleaned_data["type"].values_list("type", flat
#                                                  =True)]))    h kagouria tou sergiou pou douleuei
def show_publication(request, slug):
    # import ipdb; ipdb.set_trace()
    if request.method == "GET":
        # form = PaperForm(request.GET)
        result = Paper.objects.filter(slug__exact=slug)
        mat = PaperUsedMaterial.objects.filter(paper__slug__exact=slug)

        context = {
            # 'form': form, # ara ayto den to xreizete kan...?
            'mat': mat,
            'results': result,
            'slug': slug  # ti to ithele ayto den katalabainw
        }
    return render(request, 'search_tool_app/show_publication.html', context)


def vue_example(request):

    names = ("Takis", "Makis", "Sakis", "Lakis", "Thrasiboulos")

    items = []
    for i in range(5):
        items.append({
            "name": random.choice(names),
            "age": random.randint(20,80),
            "url": "https://example.com",
            "clicked": False
        })

    context = {}
    context["items"] = items
    context["items_json"] = json.dumps(items)

    return render(request, 'search_tool_app/vue_example.html', context=context)


def vue_search(request):
    return render(request, 'search_tool_app/vue_search.html', context={})


def vue_paper_search(request):
    return render(request, 'search_tool_app/vue_paper_search.html', context={})


