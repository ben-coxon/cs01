# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.


###########################################################################

###########################################################################


# MY ANSWER SECOND ATTEMPT (After viewing beginning of Udacity solution)

def remove_tags(string):
    start = string.find("<")
    while start != -1:
        end = string.find(">", start)
        string = string[:start] + " " + string[end+1:]
        start = string.find("<")
    string = string.split()
    return string

# The solution above is so much more elegant and simple than my first hacky attempt!


# MY ANSWER FIRST ATTEMPT

def remove_tags(string):
    output = []
    word = ""
    is_tag = False   
    new_word = False
    prevchar = ""
    
    for char in string:
        
        if char == "<":
            is_tag = True
            new_word = True                 # Set new_word to True, as tag has been opened
                                            # and therefore chars in current word should
                                            # be added to output.
        elif char == ">":
            is_tag = False
            new_word = False
            
        elif char == " " and prevchar != ">":
            new_word = True                 # Prevent spaces being added to word, and ensure 
                                            # new word is not created if a space follows a
                                            # tag closing > character.

        elif char == " ":
            continue
        
        elif char == "\n":
            new_word = True
            
        else:                               # If tag or whitespace char not detected, add
            if not is_tag:                  # add char to word.
                word = word  + char
                
        if new_word and word != "":         # If new_word is True, add new word to the
            output.append(word)             # output.
            new_word = False
            word = ""                       # Set new_word to False and initialise word
                                            # back to "" so chars can begin to be added again
                                            # for next word.
        prevchar = char
    
    if word:                                # If word still contains any remaining chars,
        output.append(word)                 # add them to output before returning
        
    return output
        
###########################################################################

# UDACITY ANSWER
        
## Same as my second solution
            
###########################################################################  
    
###########################################################################

# TESTS

print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']


text ='''<h1>Caveats follow</h1><p>Note that while this is perhaps the cleanest way to answer the question <em>as asked</em>, <code>index</code> is a rather weak component of the <code>list</code> API, and I can't remember the last time I used it in anger. It's been pointed out to me in the comments that because this answer is heavily referenced, it should be made more complete. Some caveats about <code>list.index</code> follow. It is probably worth initially taking a look at the docstring for it:</p><pre><code>&gt;&gt;&gt; print(list.index.__doc__)
L.index(value, [start, [stop]]) -&gt; integer -- return first index of value.
Raises ValueError if the value is not present.
</code></pre>'''

print remove_tags(text)