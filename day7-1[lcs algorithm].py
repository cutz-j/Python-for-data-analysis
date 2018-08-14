import numpy as np


# 레벤슈타인거리알고리즘
# 두 단어 간의 편집거리 계산
def calc_dist(word1, word2):
    lenA=len(word1)
    lenB=len(word2)
    matrix=np.zeros((lenA+1, lenB+1))
    if word1==word2:
        return matrix[lenA][lenB]
    if word1=="": return lenB
    elif word2=="": return lenA
    for i in range(lenA+1):
        matrix[i][0]=i
    for j in range(lenB+1):
        matrix[0][j]=j
    word1=" "+word1
    word2=" "+word2
    for i in range(1,lenA+1):
        for j in range(1,lenB+1):
            if word1[i]==word2[j]:
                matrix[i][j]=matrix[i-1][j-1]
            else:
                matrix[i][j]=min(matrix[i-1][j-1],matrix[i-1][j],matrix[i][j-1])+1
    print(matrix)
    return matrix[lenA][lenB]

# LCS(최장공통부분수열 알고리즘)
def lcs(word1, word2):
    lenA=len(word1)
    lenB=len(word2)
    matrix=np.zeros((lenA+1, lenB+1))
    if word1==word2:
        return matrix[lenA][lenB]
    if word1=="": return lenB
    elif word2=="": return lenA
    word1=" "+word1
    word2=" "+word2
    for i in range(1,lenA+1):
        for j in range(1,lenB+1):
            if word1[i]==word2[j]:
                matrix[i][j]=matrix[i-1][j-1]+1
            else:
                matrix[i][j]=max(matrix[i-1][j-1],matrix[i-1][j],matrix[i][j-1])
    print(matrix)
    return matrix[lenA][lenB]


samples=["신촌역","화곡역","동대문입구역","신발","상공회의소"]
r=sorted(samples, key=lambda i: calc_dist(samples[0], i))
s=sorted(samples, key=lambda j: lcs(samples[0], j))