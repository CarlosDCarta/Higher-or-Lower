import game_data, art
from random import randint

def getting_profile():
    profile_A = profile_dict[randint(0, len(profile_dict)-1)]
    profile_B = profile_dict[randint(0, len(profile_dict)-1)]
    if profile_A == profile_B:
        return getting_profile()  
    return profile_A, profile_B

def greater_following(prof_A, prof_B):
    """Function is to figure out who has higher following and to return the correct answer the program is looking for."""
    sum1 = []
    sum2 = []
    for key in prof_A and prof_B:
        if key == 'follower_count':
            sum1.append(prof_A[key])
            sum2.append(prof_B[key])           
            if sum1 > sum2:
                sum1.append('A')
                return sum1
            else:
                sum2.append('B')
                return sum2   

def user_response_process(high_foll,display_1, display_2):
    print(f"Compare A: {display_1['name']}, {display_1['description']}, from {display_1['country']}")
    print(art.vs)
    print(f"Compare B: {display_2['name']}, {display_2['description']}, from {display_2['country']}\n")

    answer = input("Type 'A', if A has higher following or type 'B', if B has a higher following:").upper()
    if answer == high_foll[1]:
        return 1
        #loop to next profiles
    else:
        return 0


#main program
profile_dict = game_data.data
record = 0

continue_game = True
while continue_game:
    profile_A, profile_B = getting_profile()
    higher_following = greater_following(profile_A, profile_B)
    score = user_response_process(higher_following,profile_A,profile_B)
    if score == 1:
        record += 1
        print(art.logo)
        print(f"Correct!Your current score is {record}")
    else:
       print("You Lost")
       continue_game = False