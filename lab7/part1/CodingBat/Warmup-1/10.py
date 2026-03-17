def front3(s):
    if len(s) < 3:
        front = s
    else:
        front = s[:3]
    return front + front + front