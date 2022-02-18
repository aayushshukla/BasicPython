noof1=int(input('enter number of singles'))
noof2=int(input('enter number of doubles'))
noof4=int(input('enter number of 4'))
noof6=int(input('enter number of 6'))
total_ball=int(input('enter total number of balls faced'))
total_ball_scored=noof1+noof2+noof4+noof6
if total_ball_scored<=total_ball:
    totalruns=noof1+2*noof2 +4*noof4+6*noof6
    dotballs=total_ball -total_ball_scored
    print('total runs scored',totalruns)
    print('dot balls ',dotballs)
else:
    print('Invalid data')
