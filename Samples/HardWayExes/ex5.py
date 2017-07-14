name = "Vishnu Vardhan Reddy"
age = 32
height = 74
weight = 180
eyes = 'Blue'
teeth = 'white'
hair = 'brown'

print "Let's talk about %s" % name
print "He is %d inches tall" % height
print "He is %d heavy" % weight
print "Actually that's not too heavy"
print "He has got %s eyes and %s hair" % (eyes, hair)
print "His teeth is %s" %teeth


print "If I add %d, %d and %d I get %d." %(age, height, weight, age + height + weight)

conv_m_to_cm_fac = 100
heightInCm = height * conv_m_to_cm_fac

print "Height in cm is %d" % heightInCm
