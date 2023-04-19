import random

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from player.models import (
    FirstName, LastName, AbilityScore, MeleeWeapon, Gear, Skill, Appearance,
    PhysicalDetail, Personality, Clothing, Secret, Background
)
from .forms import PlayerCharacterForm

def random_selection(model_class):
    return random.choice(model_class.objects.all())

class GenerateCharacterView(View):
    template_name = 'character_generator/character_generator.html'

    def get_random_data(self):
        ability_score = AbilityScore.objects.create(
            name="Abilities",
            heart=random.randint(0, 2),
            soul=random.randint(0, 2),
            body=random.randint(0, 2),
        )
        return {
            'first_name': random_selection(FirstName).name,
            'last_name': random_selection(LastName).name,
            'ability_scores': {
                'heart': ability_score.heart,
                'soul': ability_score.soul,
                'body': ability_score.body,
            },
            'melee_weapon': random_selection(MeleeWeapon).name,
            #     'gear': random_selection(Gear).name,
            'skills': random_selection(Skill).name,
            'appearance': random_selection(Appearance).name,
            'physical_details': random_selection(PhysicalDetail).name,
            'personality': random_selection(Personality).name,
            'clothing': random_selection(Clothing).name,
            'secret': random_selection(Secret).name,
            'background': random_selection(Background).name,
        }

    def get(self, request):
        random_data = self.get_random_data()
        form = PlayerCharacterForm(initial=random_data)
        return render(request, self.template_name, {'form': form})


    def post(self, request):
        if 'reroll' in request.POST and request.POST['reroll'] == 'true':
            random_data = self.get_random_data()
            return JsonResponse(random_data)

        form = PlayerCharacterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'character_generator/character_created.html')
        else:
            if 'hx-request' in request.headers:  # Check if the request is an htmx request
                return HttpResponse(form.as_p())  # Return only the updated form
            return render(request, self.template_name, {'form': form})