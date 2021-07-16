from django.shortcuts import render
from .forms import PaperForm, SearchForm, MaterialUsedForm
from .models import Language, Year, Type, Tag, Paper, PaperUsedMaterial
from functools import reduce
from django.db.models import Q
from django.urls import reverse


def homepage(request):
    context_dict = {'text1': 'Home page '}
    return render(request, 'search_tool_app/homepage.html', context=context_dict)


def post_a_publication(request):
    form = PaperForm()
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
    return render(request, 'search_tool_app/post_a_publication.html', context={'form': form})


def search_publication(request):
    form = SearchForm()
    if request.method == 'GET':
        # Provide the initial data required to render the search options

        return render(request, 'search_tool_app/search_publication.html',
                      context={'form': form}
                      )
    elif request.method == 'POST':
        # import ipdb; ipdb.set_trace()

        form = SearchForm(request.POST)

        if form.is_valid():
            title_filter = form.cleaned_data['title']
            year_filter = form.cleaned_data['year'].values_list('id', flat=True)
            type_filter = form.cleaned_data['type'].values_list('id', flat=True)
            lang_filter = form.cleaned_data['language'].values_list('id', flat=True)
            tag_filter = form.cleaned_data['tag'].values_list('id', flat=True)
            material_filter = form.cleaned_data['material'].values_list('id', flat=True)
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

            results = Paper.objects.filter(**filters_dict)
            mat_results = PaperUsedMaterial.objects.filter(**mat_filters_dict)  # not returning correct results

            return render(request, 'search_tool_app/search_publication.html', {
                'results': results,
                'mat_results': mat_results,
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
