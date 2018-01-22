from django.shortcuts import render

from models import Person


def who_we_are(request, template_name="quem_somos.html"):
    people = Person.objects.all().order_by('name')
    coordination = people.filter(coordination=True)
    members = people.filter(coordination=False)
    context = {'coordination': coordination, 'members': members}
    return render(request, template_name, context)