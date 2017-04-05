from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

from forms import PersonForm


def registration(request, template_name="faca_parte/faca_parte.html"):

    person_form = PersonForm(request.POST or None)

    if request.method == "POST":

        if request.POST['action'] == "send":

            if person_form.is_valid():

                person_form.save()
                messages.success(request, _('Registration created successfully!'))
                redirect_url = reverse("registration")
                return HttpResponseRedirect(redirect_url)

            else:
                messages.warning(request, _('Information not saved.'))

        else:
            messages.warning(request, _('Action not available.'))

    context = {"person_form": person_form}

    return render(request, template_name, context)
