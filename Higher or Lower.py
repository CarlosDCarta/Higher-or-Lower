#import dictionaries
import game_data, art
from random import randint
# ascii art and show user two options
print(art.logo, art.vs)
profile_dict = game_data.data
def getting_profile():
    profile_A = profile_dict[randint(0, len(profile_dict)-1)]
    profile_B = profile_dict[randint(0, len(profile_dict)-1)]
    if profile_A == profile_B:
        getting_profile()  
    return profile_A, profile_B

def greater_following(prof_A, prof_B):
    for key in prof_A and prof_B:
        if key == 'follower_count':
            sum1 = prof_A[key]
            sum2 = prof_B[key]
        if sum1 > sum2:
            return sum1
        else:
            return sum2   

#main program
profile_A, profile_B = getting_profile()
higher_followinf = greater_following(profile_A, profile_B)

#Process options for who has bigger following

#either keep track of score or end game

#Randomly iterarte through dictionary for next comparison

# add fault tolerance for same comparison

#Ascii art repeatedly show up for all comparisons. 





