from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Batu Sulaiman',
        'price': '999999999',
        'description': 'Batu sakral yang bisa meningkatkan stamina pengguna'
    }

    return render(request, "main.html", context)
