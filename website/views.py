# from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext


# def google_analytics(request):
#     """
#     Using the variable returned in this function to render the Google Analytics tracking code.
#     """
#     ga_prop_id = getattr(settings, 'GOOGLE_ANALYTICS_PROPERTY_ID', False)
#     if ga_prop_id:
#         return {'GOOGLE_ANALYTICS_PROPERTY_ID': ga_prop_id}
#     return {}


def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response