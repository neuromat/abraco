from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

from models import Person
from forms import PersonForm


def registration(request, template_name="faca_parte.html"):

    person_form = PersonForm(request.POST or None)

    if request.method == "POST" and request.POST['action'] == "send":
        email_typed = person_form['email'].value()

        if Person.objects.filter(email=email_typed).exists():
            messages.error(request, _("E-mail already registered"))

        if person_form.is_valid():

            person_form.save()
            messages.success(request, _('Registration created successfully!'))
            redirect_url = reverse("registration")
            return HttpResponseRedirect(redirect_url)

        else:
            messages.warning(request, _('Information not saved.'))

    context = {"person_form": person_form}

    return render(request, template_name, context)
