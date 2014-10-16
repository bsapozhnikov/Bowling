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
    game_totals = [1 for x in xrange(21)]
    balls = L[1].split(' ')
    print balls
    i = 0
    while i<18:
        if i>0:
            game_totals[i]=game_totals[i]*int(balls[i])+game_totals[i-1]
        else:
            game_totals[i]=int(balls[i])+int(balls[i+1])
        game_totals[i+1]=game_totals[i+1]*int(balls[i+1])+game_totals[i]
        print `i/2`+' '+balls[i]+' '+balls[i+1]+' '+`game_totals[i+1]`        
        i+=2

##return page
