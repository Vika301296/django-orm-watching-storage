from datacenter.models import Visit
from django.shortcuts import render

from custom_functions import format_duration


def storage_information_view(request):

    still_in_vault = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in still_in_vault:
        visit = {
            'who_entered': visit.passcard,
            'entered_at': visit.entered_at,
            'duration': format_duration(visit.get_duration()),
            'is_strange': visit.is_visit_long(),
        }
        non_closed_visits.append(visit)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
