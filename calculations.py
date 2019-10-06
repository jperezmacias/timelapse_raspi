# Calculations for the timelapse
t=30
size=1.4
npic_size=3600/t*24*size
npic=3600/t*24
minuntes=npic/(30*60)
print "Size in Mb: "+str(npic_size)
print "Number of pictures: "+str(npic)
print "Total minutes: " + str(minuntes)

