from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import get_object_or_404, render


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        visit = {
            'entered_at': visit.entered_at,
            'duration': visit.get_duration(),
            'is_strange': visit.is_visit_long()
        }
        this_passcard_visits.append(visit)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
