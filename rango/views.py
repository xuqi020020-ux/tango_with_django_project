from django.shortcuts import render

def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Xuqi.'}
    return render(request, 'rango/about.html', context=context_dict)
