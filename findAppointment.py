
# Python 3.5

def conv(hm):
    # convert h:m into minutes since 0:00
    return int(hm[0:2]) * 60 + int(hm[3:5])

def deconv(mi):
    # convert from min to h:m
    h, m = divmod(mi, 60)
    return str(h).zfill(2) + ':' + str(m).zfill(2)
    
def isBusy(schedrow, m):
    busy = 0 
    for meet in schedrow:
      # print(meet)
      if conv(meet[0]) <= m < conv(meet[1]):
        busy = 1
    return busy
    
def get_start_time(sched, duration):
    n = len(sched)
    dur = 0
    for m in range(9 * 60, 19 * 60):
      tot = sum([isBusy(sched[i], m) for i in range(n)])
      if tot > 0:
        dur = 0 # reset
      else:
        if dur == 0: start = deconv(m) # set start
        dur += 1
        # print(m, dur)
        if dur == duration:
          return start
    return None
    
sched = [[['09:00', '11:00']], [['10:30', '11:00']]]
schedules = [
  [['09:00', '11:30'], ['13:30', '16:00'], ['16:00', '17:30'], ['17:45', '19:00']],
  [['09:15', '12:00'], ['14:00', '16:30'], ['17:00', '17:30']],
  [['11:30', '12:15'], ['15:00', '16:30'], ['17:45', '19:00']]
]
print(isBusy(schedules[2], 12 * 60))
print(conv('10:00'))
print(deconv(600))
print(get_start_time(sched, 100))
print(get_start_time(schedules, 60))
