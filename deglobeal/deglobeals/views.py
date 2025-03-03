from django.shortcuts import render
# from django.http import HttpResponse

def homepage(request):
    # return HttpResponse("Hello world, i am improving on django")
    return render(request, 'home.html')

def news(request):
    # return HttpResponse("my about page, i am improving on django")
    return render(request, 'news.html')

def updates(request):
    # return HttpResponse("my about page, i am improving on django")
    return render(request, 'updates.html')

def cv_page(request):
    # return HttpResponse("my about page, i am improving on django")
    return render(request, 'cv_page.html')

def certificate(request):
    # return HttpResponse("my about page, i am improving on django")
    return render(request, 'certificate.html')

def about(request):
    # return HttpResponse("my about page, i am improving on django")
    return render(request, 'about.html')

def social(request):
    # return HttpResponse("my about page, i am improving on django")
    return render(request, 'social.html')

def email(request):
    # return HttpResponse("my about page, i am improving on django")
    return render(request, 'email.html')

def sign_up(request):
    # return HttpResponse("my about page, i am improving on django")
    return render(request, 'sign_up.html')

def login(request):
    # return HttpResponse("my about page, i am improving on django")
    return render(request, 'login.html')


def search(request):
    query = request.GET.get('q')
    results = []  # Replace with actual search logic
    return render(request, 'search_results.html', {'query': query, 'results': results})

# Create your views here.
