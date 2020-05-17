period=float(input())
longitude=float(input())
time=(period/360)*longitude
hour=float((time*60)/60)
mins=float((time*60)%60)
hour_position=float((360/12)*hour)
mins_position=float((360/60)*mins)
angle=float(mins_position-hour_position)
if angle<0:
    angle=-1*angle
if  angle==360:
    angle=0.00

print("{:2.2f}".format(angle))
