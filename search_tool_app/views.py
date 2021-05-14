from django.shortcuts import render
from .forms import PaperForm, SearchForm
from search_tool_app.models import Language, Year, Type, Tag, Paper


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
    form = SearchForm()
    if request.method == 'GET':
        # Provide the initial data required to render the search options

        return render(request, 'search_tool_app/search_publication.html',
                      context={'form': form}
                      )
    elif request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            results = Paper.objects.filter(title__icontains=form.cleaned_data["title"])
        
            return render(request, 'search_tool_app/search_publication.html', {'results': results, 'form': form})

    return render(request, 'search_tool_app/search_publication.html',
                  context={'form': form}
                  )
    # import ipdb; ipdb.set_trace()
