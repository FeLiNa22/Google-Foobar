import math

def solution(n):
    return countStaircases(n, n, False, {});
    
def countStaircases(prev_height, no_bricks_left, is_staircase, cache):
    
    # create a unique hash to find cached result
    cache_key = genCacheKey(prev_height, no_bricks_left);
    if(no_bricks_left == 0):
        return is_staircase;
    elif(cache_key in cache):
        return cache[cache_key];
    else:
        count = 0;
        # the min height is calculated using a formula i found
        # based on the fact the smallest staircase is 1 + 2 + 3 + 4 + ... = n
        for i in range(int((math.sqrt(1+8*no_bricks_left) - 1) / 2), min(prev_height,no_bricks_left + 1)):
            count += countStaircases(i, no_bricks_left-i, True, cache);
        # cache the result just found
        cache[cache_key] = count;
        return count;

def genCacheKey(a,b):
    return str(a) + ":" + str(b);

print(solution(10))