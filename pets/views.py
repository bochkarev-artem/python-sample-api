# html view
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Pets


def index(request):
    pets_list = Pets.objects.order_by('id')
    context = {
        'pets_list': pets_list,
    }
    return render(request, 'pets/index.html', context)


def detail(request, pet_id):
    try:
        pet = Pets.objects.get(pk=pet_id)
    except Pets.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'pets/detail.html', {'pet': pet})


def update(request, pet_id):
    pet = get_object_or_404(Pets, pk=pet_id)

    try:
        pet.name = request.POST['name']
    except (KeyError, Pets.DoesNotExist):
        return render(request, 'pets/detail.html', {
            'pet': pet,
            'error_message': "No name provided.",
        })
    else:
        pet.save()
        return HttpResponseRedirect(reverse('pets:detail', args=(pet.id,)))
