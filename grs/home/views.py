from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'home/home.html')


def handle_not_found(request, exception):
    ''' handle 404 exception '''
    return render(request, 'home/404.html')


def handle_server_error(request):
    ''' handle 500 exception '''
    return render(request, 'home/500.html')


def permission_denied(request, exception):
    ''' handle 403 exception '''
    return render(request, 'home/403.html')
