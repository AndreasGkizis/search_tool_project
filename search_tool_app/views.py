from django.shortcuts import render
from .forms import PaperForm
# from .models import Paper
from .filters import *


def homepage(request):
    context_dict = {'text1': 'Home page '}
    return render(request, 'search_tool_app/homepage.html', context=context_dict)


def post_a_publication(request):
    form = PaperForm()
    if request.method == 'POST':
        form = PaperForm(request.POST, request.FILES)
        if form.is_valid():
            pap = form.save(commit=True)
            pap.save()
            print(pap)
            return homepage(request)
        else:
            print(form.errors)
    return render(request, 'search_tool_app/post_a_publication.html', {'form': form})


def search_publication(request):

    papers = Paper.objects.all()

    search = PaperFilter(request.GET, queryset=papers)
    papers = search.qs

    context = {
        'search': search,
        'papers': papers,
    }
    # if request.method == "GET":
    #     papers = PaperFilter(request.POST, request.FILES)
    #     if papers.is_valid():
    #         return

    return render(request, 'search_tool_app/search_publication.html', context=context)


    # import ipdb
    # ipdb.set_trace()