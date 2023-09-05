import numpy as np

print("=====================================")
alfa = float(input("Digite o valor de alfa: "))
beta = float(input("Digite o valor de beta: "))
print("=====================================")

A = np.ones([2,2])
A[0,0] = alfa
A[1,1] = alfa
A[0,1] = beta
A[1,0] = -beta
print("\nA")
print(A)

autovalores, autovetores = np.linalg.eig(A)

print("\nlambda1 = ",str(autovalores[0]),"   autovetor1 =",autovetores[0])
print("lambda2 = ",str(autovalores[1]),"   autovetor1 =",autovetores[1])
print("")

k = np.sqrt(2)
print("Resultado não normalizado")
print("\nlambda1 = ",str(autovalores[0]),"   autovetor1 =",k*autovetores[0])
print("lambda2 = ",str(autovalores[1]),"   autovetor1 =",k*autovetores[1])
print("")



