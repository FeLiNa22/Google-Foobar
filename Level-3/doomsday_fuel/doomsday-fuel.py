from fractions import Fraction
import math
# sets the matrix into the form for markov chain partioning
#       |-----|-----|
#       |  I  |  0  |
#       |-----|-----| 
#       |  R  |  Q  |
#       |-----|-----|

# -------->
    
#       |-----|-----|
#       |  I  |  0  |
#       |-----|-----| 
#       | FR  |  0  | F = (I-Q)^-1
#       |-----|-----|

def solution(mat):
    no_of_states  = len(mat);
    
    if(no_of_states > 10 or no_of_states < 0):
        raise Exception("Invalid Argument, matrix size must be between 1-10")
    elif(no_of_states == 1):
        return [1,1];
    
    states = getStates(mat);
    
    no_terminal_states = len(states[0]);
    no_non_terminal_states = len(states[1]);
    state_index = states[0] + states[1];
    
    # calculate probabilities of non-terminal states
    # so each row has total sum = 1
    for i in states[1]:
        total = sum(mat[i]);
        for j in range(no_of_states):
            mat[i][j] = Fraction(mat[i][j], total);
    # setup R 
    R = [[0 for x in range(no_terminal_states)] for y in range(no_non_terminal_states)];
    for i in range(no_terminal_states, no_of_states):
        row = state_index[i];
        for j in range(no_terminal_states):
            R[i - no_terminal_states][j] = mat[row][state_index[j]] 
    # setup and calculate (I-Q)      
    Q = [[0 for x in range(no_non_terminal_states)] for y in range(no_non_terminal_states)];
    for i in range(no_terminal_states, no_of_states):
        row = state_index[i];
        for j in range(no_terminal_states, no_of_states):
            # added (i==j)-mat.. to simultaneously calculate (I-Q)
            Q[i-no_terminal_states][j-no_terminal_states] = (i==j) - mat[row][state_index[j]]
    # F = (I - Q)^-1
    F = inverseMat(Q);
    # FR = F x R using matrix multiplication
    FR = multiplyMat(F, R);
    
    # By the setup, State 0 -> terminating state is always the 1st row of FR
    # so we just work with this
    # get the lowest common multiple
    lcm = find_lcm(FR[0])
    # convert the row from fractions to integers
    result = list(map(lambda x: int(x * lcm), FR[0]))
    result.append(lcm)
    return result;

def find_lcm(fractions):
   lcm = fractions[0].denominator
   for d in fractions[1:]:
        lcm = lcm // math.gcd(lcm, d.denominator) * d.denominator
   return lcm;
# multiplies two N x N matrices 
# as max size is 10 use standard algorithm, for larger matrices I would use the strassen method
def multiplyMat(A, B):
    rows = len(A)
    if(len(A) == 0):
        return []
    cols = len(B[0])
    res = [[0 for x in range(cols)] for y in range(rows)]
    for i in range(rows):
        for k in range(len(B)):
            for j in range(cols):
                res[i][j] += A[i][k] * B[k][j];
    return res

# uses gaussian elimination to find matrix inverse
def inverseMat(mat):
    n = len(mat);
    a = [[0 for x in range(2 * n)] for y in range(n)]
    solution = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            a[i][j] = mat[i][j]
    
    # Augmenting Identity Matrix of Order n
    for i in range(n):        
        a[i][i+n] = 1
    
    # Applying Guass Jordan Elimination
    for i in range(n):
        if(a[i][i] == 0):
            continue
        for j in range(n):
            if i != j:
                ratio = a[j][i]/a[i][i]
    
                for k in range(2*n):
                    a[j][k] = a[j][k] - ratio * a[i][k]
    
    # Row operation to make principal diagonal element to 1
    for i in range(n):
        divisor = a[i][i]
        if(divisor == 0):
            continue;
        for j in range(2*n):
            a[i][j] = a[i][j]/divisor
    
    for i in range(n):        
        for j in range(n):
            solution[i][j] = a[i][j+n];
    return solution;

# returns a list of [[terminal states],[non-terminal states]]
def getStates(mat):
    no_of_states = len(mat);
    states = [[],[]]
    for i in range(no_of_states):
        terminal = True;
        for j in range(no_of_states): 
            if(mat[i][j] > 0):
                terminal = False;
                break;
        if(terminal):
            states[0].append(i);
        else:
            states[1].append(i);
    return states

print(solution(
        
       [
        [2,1,1],
        [0,0,0],
        [0,0,0]
    ]
    
    ))