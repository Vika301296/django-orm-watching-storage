SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600


def format_duration(duration):
    duration = duration.total_seconds()
    hours = int(duration // SECONDS_IN_HOUR)
    remaining_seconds = duration % SECONDS_IN_HOUR
    minutes = int(remaining_seconds // SECONDS_IN_MINUTE)
    duration = f'{hours} ч. {minutes} мин.'
    return duration
