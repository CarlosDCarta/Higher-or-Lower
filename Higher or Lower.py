#import dictionaries
import game_data, art
from random import randint
# ascii art and show user two options
print(art.logo, art.vs)
profile_dict = game_data.data
def getting_profile():
    profile_A = profile_dict[randint(0, len(profile_dict))]
    profile_B = profile_dict[randint(0, len(profile_dict))]
    if profile_A == profile_B:
        getting_profile()
    print(profile_A,"\n",profile_B)
getting_profile()
#Process options for who has bigger following

#either keep track of score or end game

#Randomly iterarte through dictionary for next comparison

# add fault tolerance for same comparison

#Ascii art repeatedly show up for all comparisons. 





