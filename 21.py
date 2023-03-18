def maw(msl,ms):
    max_visit=0
    P=msl.count('P')
    E = msl.count('E')
    O=msl.count('O')

    if P>E and P>O:
        s=ms['P']
    elif E>O:
        s=ms['E']
    else:
        s=ms['O']
    return s
msl=[301,'P',302,'P',305,'P',401,'E',656,'E']
ms={"P":'pediatrics',"O":'orthopredics',"E":'ent'}
s=maw(msl,ms)
print(s)
