# http://www.pythonchallenge.com/pc/def/0.html
# Hint: try to change the URL address. 
# On http://www.pythonchallenge.com/pc/def/1.html
#   2**38 is much much larger.

import webbrowser

webbrowser.open('http://www.pythonchallenge.com/pc/def/' + str(2**38) + '.html')
