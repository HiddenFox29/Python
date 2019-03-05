# a - открывает и на запись и на чтение. Если файла нет, то функция его создат
# r - открывает на чтение
# w - открывает на запись. Если файла нет, то функция его создат
 
#file=open('stih.txt','r')
#print(file.read())
 
userData = ['Ivan Petrov', '12345678', 'petrov@deneg.est', '8800 88766554']
 
file = open('IvanPetrov19281.txt','w')
 
for data in userData:
    file.write(data+'\n') # \t - табуляция
 
file.close()