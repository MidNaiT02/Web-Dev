def cigar_party(cigars, is_weekend):
    return cigars >= 40 if is_weekend else cigars in range(40, 61)

def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1
    
def squirrel_play(temp, is_summer):
    if is_summer:
        return 60 <= temp <= 100
    else:
        return 60 <= temp <= 90
    
def caught_speeding(speed, is_birthday):
  if is_birthday:
    if speed<=65:
      return 0
    elif speed in range(66, 86):
      return 1
    else:
      return 2
  else:
    if speed<=60:
      return 0
    elif speed in range(61, 81):
      return 1
    else:
      return 2
    
def sorta_sum(a, b):
  sum=a+b
  if sum in range(10,20):
    return 20
  else:
    return sum

def alarm_clock(day, vacation):
    if day not in [0, 6]:  # weekday
        if not vacation:
            return "7:00"
        else:
            return "10:00"
    else:  # weekend
        if not vacation:
            return "10:00"
        else:
            return "off"
        
def love6(a, b):
    return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6

def in1to10(n, outside_mode):
    if n == 1 or n == 10:
        return True
    return (n in range(1, 11)) ^ outside_mode

def near_ten(num):
    within = num % ((num / 10) * 10) if num >= 10 else num
    return within in [8, 9, 0, 1, 2]