t = 1
c = 50
r = .05
p = c*(1 + r)**t
print p

x = 2.5
y = 3.2
w = x * y
z = (w**3 + 3*x**2 + 5*y + 10)/(5*x+3)
print z

x = 5
y = 3
z = 1.0 + x/y
result = "The result of this is" + str(z)
print result

print "The result of this is " + str( 1.0 + 5.0/3.0 )

test = (5 == 3)
print test

x = 5
if( x < 5 ):
    print "x is less than 5"
else:
    print "x is NOT less than 5"
    
its_thursday = True
its_after6 = True
its_before9 = True
if( its_thursday and its_after6 and its_before9 ):
    print "You must be in Astronomy Lab!"
else:
    print "You are not in Astronomy Lab"

returned_phone_call = False
days_since_call = 3
travels_for_work = False
if( returned_phone_call ):
    print "Congratulations! He likes you."
else:
    if( days_since_call <= 2 or travels_for_work ):
        print "Give it time ... he may still be interested."
    else:
        print "He's just not that in to you."

planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]
print planets


primes = []
for i in range(0,1000):
    isPrime = True
    for j in range(2,i):
        if( i%j == 0 ):
            isPrime = False
    if( isPrime ):
        primes.append(i)
print primes