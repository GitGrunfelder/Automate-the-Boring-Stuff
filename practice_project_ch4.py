import random

# def list_to_string(list):
#     return ', '.join(list[:-1]) + ", and " + list[-1] # This function returns a joined list, using the delimiter specified
#                                                       # before the method. It goes until the last item, and concatenates
#                                                       # the item after ', and'. Will work on all lengths of list.

# list1 = ['apples', 'bananas', 'tofu', 'cats']
# print(list_to_string(list1))
#______________________________________________________________________________________________________________________________________

def flip_lists():
    
    h_t_list = []
    
    for i in range(100):
        if random.randint(0,1) == 0:
            result = 0 # Tails
        else:
            result = 1 # Heads
        h_t_list.append(result)
    return h_t_list

def streak(h_t_list):
    global numberOfStreaks # adjusts global streak variable
    head_count = 0 # local heads
    tail_count = 0 # local tails
    for i in h_t_list: # for each item in 100 flip list
        if h_t_list[i] == 1: # Heads
            tail_count = 0 # Tails reset to 0
            head_count += 1 # Heads tally
            if head_count == 6: # Once 6 reached, with no resets, increase main streak count
                numberOfStreaks += 1
                head_count = 0 # reset head count after 6 reached.
        else:# if tails
            head_count = 0 # reset head streak tally
            tail_count += 1 # increase tails tally
            if tail_count == 6: # Once 6 reached, with no resets, increase main streak count
                numberOfStreaks += 1 
                tail_count = 0 # reset once 6 reached.
        

numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that runs the coin flip 100 times, creates list of results.
    list = flip_lists()
    
    # Checks for streak of 6 H or 6 T
    streak(list)
    
print(f"You had {numberOfStreaks} streaks of either 6 heads or 6 tails in a row in one million coin flips.")
print('Chance of streak: %s%%' % (numberOfStreaks / 10000))


