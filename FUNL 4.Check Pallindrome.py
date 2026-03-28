lst=["madam","python","malayalam",12321]
result=list(filter(lambda s:str(s)==str(s)[::-1],lst))
print(result)