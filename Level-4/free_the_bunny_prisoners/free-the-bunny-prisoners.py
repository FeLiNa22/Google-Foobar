from itertools import combinations 

def solution(num_buns, num_required):
    # keys assigned to each bunny
    keys = [[] for num in range(num_buns)]
    if(num_buns < num_required):
        return keys;
    # as num_required-1 bunnies cant open the door
    # there must be (num_buns CHOOSE num_buns - num_required + 1) distinct keys
    for key, comb in enumerate(combinations(range(num_buns), num_buns - num_required + 1)):
        for b in comb:
            keys[b].append(key)
    return keys

    
    
print(
      solution(5, 3)
)