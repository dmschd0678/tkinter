kor = ["사과","바나나","오렌지"]
eng = ['apple','banana','orange']

print(list(zip(kor,eng))) # zip 묶기

mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]
print(list(zip(*mixed))) # zip 풀기

kor2, eng2 = zip(*mixed)
print(kor2)
print(eng2)