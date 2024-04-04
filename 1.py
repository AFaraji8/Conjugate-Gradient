import numpy as np

A=np.matrix([[1,1/2,1/3],[1/2,1/3,1/4],[1/3,1/4,1/5]])
print("A:")
print(A)

B=np.matrix([[5/6],[5/12],[17/60]])
print("B:")
print(B)

X=np.matrix([[0],[0],[0]])
print("X:")
print(X)


C=B-(A*X)
print("C(r):")
print(C)


D=B-(A*X)
print("D:")
print(D)
print("\n")

for i in range(0,5):

    print("NEW RAND (",i,"):")

    print("\nX:")
    print(X)
    print("\n")

    print("\n D:")
    print(D)
    print("\n")


    


    C=B-(A*X)
    print("C(r):")
    print(C)
    print("\n")


    #alfa=
    g=(np.matrix.transpose(D)*C/(np.matrix.transpose(D)*A*D))[0,0]
    

    print("g(alpha):")
    print(g)
    print("\n")


    F= X + (g*D)
    print("F(new X):")
    print(F)
    print("\n")


    
    print("A*F-B:")
    print(A*F-B)
    print("\n")







    #beta=
    h= (np.matrix.transpose(D)*A*((A*F)-B)/(np.matrix.transpose(D)*A*D))[0,0]
    print("h(beta):")
    print(h)
    print("\n")

    DD= B-(A*F)+(h*D)
    print("DD:")
    print(DD)

    X=F
    D=DD
    print("\n")
    print("\n")
    print("\n")




    
