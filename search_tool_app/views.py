from django.shortcuts import render
from search_tool_app.forms import PaperForm


def homepage(request):
    context_dict = {'text1': 'Home page '}
    return render(request, 'search_tool_app/homepage.html', context=context_dict)


def post_a_publication(request):
    form = PaperForm()
    if request.method == 'POST':
        form = PaperForm(request.POST)
        if form.is_valid():
            pap = form.save(commit=True)
            pap.save()
            print(pap)
            return homepage(request)
        else:
            print(form.errors)
    return render(request, 'search_tool_app/post_a_publication.html', {'form': form})

# import ipdb
# ipdb.set_trace()