from django.shortcuts import render
from .forms import UserRegister
from django.http import HttpResponse

# Псевдо-список пользователей
users = ['Tom', 'Pop', 'Kok', 'Ivan', 'Puk']
def sign_up_by_django(request):
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = "Пароли не совпадают"
            elif age < 18:
                info['error'] = "Вы должны быть старше 18"
            elif username in users:
                info['error'] = "Пользователь уже существует"
            else:
                info['welcome_message'] = f"Приветствуем, {username}!"  # Приветственное сообщение
        info['form'] = form
    else:
        form = UserRegister()
        info['form'] = form

    return render(request, 'fifth_task/registration_page_1.html', context=info)


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        age = int(age)

        print(f'Username: {username}')
        print(f'password: {password}')
        print(f'repeat_password: {repeat_password}')
        print(f'age: {age}')

        if password != repeat_password:
            info['error'] = "Пароли не совпадают"
        elif age < 18:
            info['error'] = "Вы должны быть старше 18"
        elif username in users:
            info['error'] = "Пользователь уже существует"
        else:
            info['welcome_message'] = f"Приветствуем, {username}!"  # Приветственное сообщение

        return HttpResponse('Форма успешно отправлена')

    return render(request, 'fifth_task/registration_page.html', context=info)

