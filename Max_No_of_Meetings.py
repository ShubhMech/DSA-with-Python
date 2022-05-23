l= []

class Meetings:
    def __init__(self,s,f,pos):
        self.start= s
        self.end= f
        self.pos= pos

s = [ 1, 3, 0, 5, 8, 5 ]
f = [ 2, 4, 6, 7, 9, 9 ]

for i in range(len(s)):
    l.append(Meetings(s[i],f[i],i))
    
l.sort(key= lambda x : x.end)

def max_meetings():
    m_1 = l[0]
    cutoff = l[0].end

    meetings = 1
    list_meeting= [l[0].pos]
    
    for i in range(1,len(l)):
        if l[i].start >= cutoff
        meetings +=1
        list_meeting.append(l[i].pos)
