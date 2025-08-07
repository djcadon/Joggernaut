from datetime import timedelta

def consolidate_time(time_mins):
    ret = ''
    if time_mins < 1:
        ret += str(round(time_mins * 60, 2))
        ret += ' s'
    
    else:
        ret += str(round(time_mins, 2)) + ' mins'
    
    return ret
