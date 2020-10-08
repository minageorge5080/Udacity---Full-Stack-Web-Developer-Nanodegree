import urllib

def read_text():

    quotes =  open('/Users/minageorge/workSpaces/python/udacity/classes/assets/movie_quotes.txt')
    content = quotes.read()
    quotes.close()
    check_profanity(content)

def check_profanity(text_check):
    connection = urllib.urlopen('http://www.wdylike.appspot.com/?q='+text_check)
    output = connection.read()
    connection.close()
    if "true" in output:
        print("Profanity Alert !!")
    else :
        print("No curse words")    

read_text()    