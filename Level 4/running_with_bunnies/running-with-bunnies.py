from itertools import permutations 

# taken the apprach of using the bellman-ford algorithm to
# find the min distance between a single source node and every other node

def solution(times, time_limit):
    no_checkpoints = len(times);
    no_bunnies = no_checkpoints - 2;
    if(no_bunnies > 5 or no_bunnies < 1 or time_limit > 999 or time_limit < 1):
        raise Exception("Invalid Argument Exception");
        
    d = [[float('inf') for x in range(no_checkpoints)] for y in range(no_checkpoints)]
    # no point in terminating bellman-ford algorithm early
    # as input size is very small
    for x in range(no_checkpoints):
        d[x][x] = 0;
        for i in range(no_checkpoints - 1):
            for u in range(no_checkpoints):
                for v in range(no_checkpoints):
                    d[x][v] = min(d[x][v], d[x][u] + times[u][v]);
                        
    # determines if negative cycle is present in graph
    # by checking if a smaller path can still be found
    for u in range(no_checkpoints):
        for v in range(no_checkpoints):
            if(d[0][v] > d[0][u] + times[u][v]):
                # if there is a negative cycle
                # all the bunnies can be saved. YAY!
                return range(no_bunnies);
    
    # go through each permutation of bunnies starting with the largest
    counter = no_bunnies;
    while(counter > 0):
        for perm in permutations(range(no_bunnies), counter):
            print(perm)
            cost = 0;
            # start checkpoint
            prev = 0;
            # intermediate bunny nodes
            for bunny in perm:
                cost += d[prev][bunny + 1]
                prev = bunny + 1;
            # end checkpoint
            cost += d[prev][-1];
            if(cost <= time_limit):
                return sorted(perm)
        counter -= 1;
    return []

print(
      solution(
             [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3
              )
      )