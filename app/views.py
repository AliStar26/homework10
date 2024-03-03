from django.shortcuts import render
from .models import FootballClub



def title(request):
    clubs = FootballClub.objects.all()

    for club in clubs:
        club.title = f"{club.title} ({club.id})"
        club.save()

    remove = []
    for club in clubs:
        if any(int(title) % 2 != 0 for title in club.title):
            remove.append(club)

    for club in remove:
        club.delete()

    return render(request, 'template.html', {'clubs': FootballClub.objects.all()})


