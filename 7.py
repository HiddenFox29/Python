#install html2text #библиотека 



import requests
import html2text

rewHtml = requests.get('http://google.de')
text = html2text.html2text.handle(rawHtml.text)
print(text)