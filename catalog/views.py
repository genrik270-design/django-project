from django.shortcuts import render
context = {}

def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Новое сообщение от {name} ({phone}): {message}')

        context['success'] = True
        context['user_name'] = name

    return render(request, 'catalog/contacts.html', context)
