import ipdb
from lib import *

# Test your code below...



kevin = Actor("kevin")
john = Actor("john")
adam = Actor("adam")

godzilla = Role("godzilla")
batman = Role("batman")

kevin1A = Audition("chicago", godzilla, kevin )
john1A = Audition("new york", godzilla, john )
adam1A = Audition("san fran", godzilla, adam )

kevin2A = Audition("chicago", batman, kevin )
john2A = Audition("new york", batman, john )
adam2A = Audition("san fran", batman, adam )



# the below line allows us to stop & try stuff!
ipdb.set_trace()