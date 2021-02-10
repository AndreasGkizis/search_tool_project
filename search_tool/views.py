from django.shortcuts import render


def homepage(request):
    context_dict = {'text1': 'Home page '}
    return render(request, 'search_tool/homepage.html', context=context_dict)
