import nltk
def typeq(sentences):
    sentence = sentences.lower()
    sent=nltk.pos_tag(nltk.word_tokenize(sentence))
    sen1=""
    sen2=""
    for c in sent:
        sen1=sen1+c[0]+" "
        sen2=sen2+c[1]+" "
    sent1=nltk.word_tokenize(sen1)
    sent2=nltk.word_tokenize(sen2)
    dos = ['CD','IN','JJ','JJR','JJS','MD','NN','NNP','NNPS','NNS','PDT','POS', 'RBS','RP','VB','VBG','VBD','VBN','VBP','VBZ'] #pos_tags who comes along with a question tag make it a question
    dosaf=['DT','CD'] #pos_tags whose presence along with a verb makes it a affirmation
    cato=['what','when','who'] #question_tags
    cata=['is','does''do','are','can','could','may''should'] #affirmation question tags
    if sent1[0] in cato:        #checks whether first word is a question tag
        if sent1[0]=='what':    #ambigous condition
            if sent1[1]=='time':
                    typeo = 'when'
        elif sent2[1] in dos:            #checks whether 2nd word is in dos
                typeo = sent1[0]
    elif sent1[0] in cata:      #checks whether the first word is an affirmation word 
        if sent2[1] in dosaf:  #checks whether 2nd word is in dosaf
                typeo = "Affirmation"
    elif sent2[0]=='IN':        #checks whether pos_tag of first word is 'IN'
        if sent1[1] in cato:    #checks whether 2nd word is a question tag
                typeo = sent1[1]
    else:
        typeo = 'Unknown'
    print("Type of the is question is : ",typeo)
            
        
    
