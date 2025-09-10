from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406431100',
        'name': 'Tiara Widyaningrum',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)