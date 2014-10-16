#!/usr/bin/python
import cgi, cgitb
cgitb.enable()
form = cgi.FieldStorage()

page='Content-Type: text/html\n\n'

f = open('bowling.html','r')
page+=f.read()
f.close

f = open('scores.txt','r')
people = f.readlines()
f.close()
for player in people:
    L = player.strip('\n').split('|')
    name = L[0]
    print name
    ball_totals = [0 for x in xrange(21)]
    balls = L[1].split(' ')
    print balls
    i = 0
    while i<20:
        if i>1:
            if int(balls[i-2])==10:
                ball_totals[i-1]+=int(balls[i])+int(balls[i+1])
            elif int(balls[i-2])+int(balls[i-1])==10:
                ball_totals[i-1]+=int(balls[i])
        
        if i>0:
            ball_totals[i]=int(balls[i])+ball_totals[i-1]
        else:
            ball_totals[i]=int(balls[i])
       
        ball_totals[i+1]=int(balls[i+1])+ball_totals[i]
        i+=2
    ball_totals[20]=ball_totals[19]+int(balls[20])
    print ball_totals
    frame_totals = [ball_totals[i*2+1] for i in xrange(10)]
    frame_totals[-1]+=int(balls[20])
    print frame_totals

##return page
