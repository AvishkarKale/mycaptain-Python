def most_frequent(word):
    word_letters=[]
    counting_letters={}
    count=0
    while count<len(word):
        if word[count] not in word_letters:
            word_letters.append(word[count])
        count=count+1
        
    counting_letters={}
    j=0
    while j<len(word_letters):
        i=0
        k=0
        while i<len(word):
            if word_letters[j]==word[i]:
                k=k+1
                counting_letters[word_letters[j]]=k
            i=i+1
        j=j+1
    return counting_letters
        
    
    
word=input("Enter a string :")
most_frequent(word)
print(most_frequent(word))