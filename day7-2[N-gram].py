import re

# N-gram
def split(text, n):
    pattern=re.compile("[\W\w\s]{1,%d}" %n)
    res=pattern.findall(text)
    if len(res[-1])!=n:
        res[-1]=text[len(text)-n:len(text)+1]
    return res
    

def ngram(sa, sb, num):
    saList=split(sa, num)
    sbList=split(sb, num)
    cnt=0
    r=[]
    for i in saList:
        for j in sbList:
            if i==j:
                cnt+=1
                r.append(i)
    return cnt/len(saList)
#    if len(saList) > len(sbList):
#        return cnt/len(saList)
#    else: return cnt/len(sbList)




a="오늘 상공회의소에서 문자 비교 알고리즘을 배웠다"
b="문자간 비교하는 알고리즘을 상공회의소에서 오늘 배웠다"
# 2-gram
print(ngram(a,b,2))

# 3-gram
print(ngram(a,b,3))