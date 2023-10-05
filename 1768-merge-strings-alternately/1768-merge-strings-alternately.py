class Solution(object):
    def mergeAlternately(self, word1, word2):
        new_string = ""
        if len(word1) >= len(word2):
            shortest = word2
            longest = word1
        else:
            shortest = word1
            longest = word2
        for i in range (len(shortest)):
            new_string += word1[i]
            new_string += word2[i]
            ind = i
        new_string += longest[i+1:]

        print(new_string)
        return(new_string)


        