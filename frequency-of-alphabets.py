def most_frequent(word):
    
    """
    function docstring
    ----------------------
    entering as word as string input
    :enter - most_frequent(word="the word in which you want to find frequency of alphabets")
    """
    word=word.lower()
    word_letters=[]
    counting_letters={}
    word_letters.clear()
    counting_letters.clear()
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