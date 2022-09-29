def mostWordsFound(self, sentences):
        result = 0
        for sentence in sentences:
            word_count = 0
            sentence = sentence.split(' ')
            for word in sentence:                
                word_count += 1
            if word_count > result:
                result = word_count
        return result
