# bounce.py
#
# Exercise 1.5

height_bounce = 10
num_bounces = 0
frac_nxt = 0.6 # 3/5

while num_bounces<10:
    height_bounce = height_bounce*frac_nxt
    num_bounces = num_bounces+1
    print(' Bounce = ',num_bounces, 'Height = ',round(height_bounce,4))