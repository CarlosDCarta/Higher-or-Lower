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
    """Function is to figure out who has higher following and to return the correct answer the program is looking for."""
    sum1 = []
    sum2 = []
    for key in prof_A and prof_B:
        if key == 'follower_count':
            sum1.append(prof_A[key])
            sum2.append(prof_B[key])
            print(sum1, sum2)           
            if sum1 > sum2:
                sum1.append('A')
                return sum1
            else:
                sum2.append('B')
                return sum2   

def user_response_process(high_foll):
    answer = input("Type 'A', if A has higher following or type 'B', if B has a higher following:").upper()
    if answer == high_foll[1]:
        print("correct")
        #loop to next profiles
    else:
        return'wrong'

#main program
profile_A, profile_B = getting_profile()
higher_following = greater_following(profile_A, profile_B)
user_response_process(higher_following)
#either keep track of score or end game

#Randomly iterarte through dictionary for next comparison

#Ascii art repeatedly show up for all comparisons.


