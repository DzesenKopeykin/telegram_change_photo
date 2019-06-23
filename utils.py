from datetime import datetime


def convert_time_to_string(dt):
    return dt.strftime('%H:%M')


def time_has_changed(prev_time):
    return convert_time_to_string(datetime.now()) != prev_time
