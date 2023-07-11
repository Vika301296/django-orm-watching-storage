from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):

    still_in_vault = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []

    def format_duration(duration):
        duration = duration.total_seconds()
        hours, minutes = int(duration // 3600), int(duration // 60)
        duration = f'{hours} ч. {minutes} мин.'
        return duration

    for visit in still_in_vault:
        visit = {
            'who_entered': visit.passcard,
            'entered_at': visit.entered_at,
            'duration': format_duration(visit.get_duration()),
        }
        non_closed_visits.append(visit)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
