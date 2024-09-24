import numpy as np

#test function: f(x) = x^2 - 4 one answer is 2
def f(x):
    return x ** 2 - 4

#input: g is function g(x )that has a root, there exists a x when g = 0; pos is the first bound; neg is the second negative bound; t is tolerance
#output: final approximation of the root of g
def bisectionRootFinding(g, pos, neg, t):

    #Start iteration at 0, choose one of the 2 bounds to be the approximation to start
    n = 0
    approximation = pos

    #Just in case parameters are entered wrong
    if g(pos) <= 0 and g(neg) >= 0:
        print("Swap the second and third parameters!")
        return None
    elif g(pos) < 0:
        print("Second parameter is wrong!")
        return None
    elif g(neg) > 0:
        print("Third parameter is wrong!")
        return None
    
    #Maybe starting bounds are the answer already
    if g(pos) == 0:
        print("\nFinal approximation:\n" + str(approximation))
        return approximation
    elif g(neg) == 0:
        approximation = neg
        print("\nFinal approximation:\n" + str(approximation))
        return approximation

    #Continue iteration if PC doesnt doesnt reach "0"
    while g(approximation) != 0:

        #Update new approximation using bisection
        approximation = (pos + neg) / 2
        yValue = g(approximation)

        #Check to see the new approximation is within tolerance
        if(abs(yValue) < t):
            break

        #Otherwise update the new pos or neg
        elif yValue > 0:
            pos = approximation
        else:
            neg = approximation

        #Increment iteration
        n += 1

        #Log each iteration
        print("Iteration:", n, "\t\tApproximation:", approximation)

    #Print final approximation
    print("\nFinal approximation:\n" + str(approximation))
    return approximation

#execute function     
answer = bisectionRootFinding(f, 3, 1.9, .00000001)

#Get relative error
error = abs(answer-2) / abs(2)
print("\nRelative error:\n" + str(error))