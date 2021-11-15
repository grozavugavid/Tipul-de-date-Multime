A=int(input("Dati elementele multimii A:"))
B=int(input("Dati elementele multimii B:"))
if type(A) is int:
    print('Intersectia multimilor A si B-',A.intersection(B))
print('Reuniunea multimilor A si B-',A.union(B))
print('Diferenta multimilor A si B-',A.difference(B))
print('Diferenta multimilor B si A',B.difference(A))