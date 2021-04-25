from django.shortcuts import render
from .forms import PaperForm
from .models import Language, Year, Type, Tag


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

    if request.method == 'GET':
        # Provide the initial data required to render the search options
        context = {
            "languages": Language.objects.all(),
            "years": Year.objects.all(),
            "tags": Tag.objects.all(),
            "types": Type.objects.all(),
            "results": []
        }

    elif request.method == 'POST':
        # provide with result data to be bale to render
        context = {

        }

        pass

    return render(request, 'search_tool_app/search_publication.html', context=context)



    # import ipdb; ipdb.set_trace()