#!/usr/bin/python
import cgi, cgitb
cgitb.enable()
form = cgi.FieldStorage()

page='Content-Type: text/html\n\n'

f = open('./bowling.html','r')
page+=f.read()
f.close

f = open('./scores.txt','r')
people = f.readlines()
f.close()

##new game
if 'player' in form:
    player_names = [person.split('|')[0] for person in people]
    player_games = [person.split('|')[1:] for person in people]
    new_names = form.getlist('player')
    for i in len(new_names):
        new_name = new_names[i]
        new_scores = ' '.join([form.getlist('ball'+j)[i] for j in xrange(0,21)])
        player_games[player_names.find(new_name)]+='|'+new_scores
    g = open('./scores.txt','w')
    for i in len(player_names):
        g.write(player_names[i]+'|'+player_games[i]+'\n')
    g.close()
        
##print html
tabledata=''
js = ''
for player in people:
    L = player.strip('\n').split('|')
    ##print 'L: '+`L`
    name = L[0]
    ##print name
    ball_totals = [0 for x in xrange(21)]
    games = []
    player_totals = []
    total_pins = 0
    for game in L[1:]:
        balls = game.split(' ')
        ##print balls
        i = 0
        while i<20:
            if i>1:
                if int(balls[i-2])==10:
                    if int(balls[i-4])==10:
                        ball_totals[i-3]+=int(balls[i])
                        ball_totals[i-1]+=int(balls[i])
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
        ##print ball_totals
        frame_totals = [ball_totals[i*2+1] for i in xrange(10)]
        frame_totals[-1]+=int(balls[20])
        ##print frame_totals
        games.append(balls)
        player_totals.append(frame_totals)
        total_pins+=frame_totals[-1]

    tabledata+='<tr><td>'+name+'''<input type="button" value="button" onclick="toggle(\''''+name+'''\')"></input></td>'''
    tabledata+='<td>'+`len(games)`+'</td>'
    tabledata+='<td>'+`total_pins`+'</td>'
    tabledata+='<td>'+`1.0*total_pins/len(games)`+'</td></tr>'
    js+='var '+name+'scores = '+`games`+';\n'
    js+='var '+name+'totals = '+`player_totals`+';\n'

##print tabledata
##print js    
##print 'td here' in page
page = page.replace('td here',tabledata)
page = page.replace('//py vars here',js)
print page
##return page