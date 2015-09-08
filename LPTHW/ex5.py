my_name = 'Daniel Zhang'
my_age = 18
my_height = 73
my_weight = 150
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'black'

print "Let's talk about %s." % my_name
print "He's %d cm tall." % (my_height * 2.54)
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "Hes got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usueally %s depending on the coffee." % my_teeth

# This line is tricky, try to get it exactly right

print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

print round(1.5)