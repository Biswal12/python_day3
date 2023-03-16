sentences=["a new world record was set","in the holy city of ayodhya",
           "on the eve of dawali on tuesday","with over three lakh diya or earthen lamp",
           "lit up samentenously on the bank of the sarayu river"]
stopwords = ['for','a','of','the','and','to','in','on','with','was']
result=[]
for sentence in sentences:
    row_data=[]
    for word in sentence.split():
        if word not in stopwords:
            row_data.append(word)
    result.append(row_data)
print(result)
print([[word for word in sentence.split() if word not in stopwords]for sentence in sentences])