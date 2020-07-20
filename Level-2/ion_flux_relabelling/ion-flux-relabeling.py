def solution(h, q):
    if(h < 1 or h > 30):
        raise Exception("Invalid Argument : flux converter height should only take values between 1-30")
    root = 2**h - 1;
    #initialize a fixed size output array
    output = [None] * len(q);
    
    # for some speedup performance
    # if any of q is within a certain range 
    for i in range(0,len(q)):
        if(q[i] >= root or q[i] <= 0):
            output[i] = -1;
        elif(q[i] > root - h):
            output[i] = q[i]+1;
            
    searchSubtree(root, root >> 1, output, q)
    return output

def searchSubtree(root, size, output, q):            
    if(size == 0):
        return;
    
    right = root - 1;
    
    left = right - size;
    
    idx1 = getIndex(left, q);
    if(idx1 >= 0):
        output[idx1] = root;
        
    idx2 = getIndex(right, q);        
    if(idx2 >= 0):
        output[idx2] = root;
        
    searchSubtree(left, size >> 1, output, q);
    
    searchSubtree(right, size >> 1, output, q);
    return;
    
    
def getIndex(value, xs):
    for idx in range(0, len(xs)):
        if(value == xs[idx]):
            return idx;
    return -1;

print("\n" +str(solution(5, [19, 14, 28])))