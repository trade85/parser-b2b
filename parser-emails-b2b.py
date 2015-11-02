#coding: utf-8
import re
from urllib2 import urlopen
import urllib

open('mails.txt', 'w')

print """ 
227: ЛЕСОПИЛОМАТЕРИАЛЫ — ПРОИЗВОДСТВО, ПРОДАЖА;
126: ДЕРЕВООБРАБАТЫВАЮЩАЯ ПРОМЫШЛЕННОСТЬ — ПРОИЗВОДСТВО, ПРОДАЖА ПРОДУКЦИИ;
127: ДЕРЕВООБРАБАТЫВАЮЩИЕ СТАНКИ, ОБОРУДОВАНИЕ, ИНСТРУМЕНТЫ -- ПРОИЗВОДСТВО, ПРОДАЖА;
50:  БЕТОН — ПРОИЗВОДСТВО, ПРОДАЖА;
189: КИРПИЧ — ПРОИЗВОДСТВО, ПРОДАЖА;
218: КРАСКИ, ЛАКИ, ЭМАЛИ — ПРОИЗВОДСТВО, ПРОДАЖА;
"""
number = raw_input('Введите код рубрики - ')

url = "http://b2b-russia.ru/rubricator/company/0/0/" + number + "/"

strc = 1

if number == '126':
   strc = 163
if number == '127':
   strc = 111
if number == '227':
   strc = 321
if number == '50':
   strc = 160
if number == '189':
   strc = 158
if number == '218':
   strc = 232

i = 1
while (i<=strc):
   
	html = urllib.urlopen(url + str(i) + "/0").read()
	mail = re.findall(r'[-_0-9a-zA-Z.]+@[-_0-9a-zA-Z.]+', html)
	for m in mail:
		aa = m + ','
		open('mails.txt', 'a'). write(aa)
	print ('Обработанно страниц - ' + str(i))
	i += 1
	#фильтруем мэйлы


filt = open('mails.txt').read()
dmail = filt.split(',')

fmail = []
for d in dmail:
	if d not in fmail:
		fmail.append(d)
open('mails.txt', 'w')

for z in fmail:
		gg = z + '\n'
		open('mails.txt', 'a'). write(gg)


print("Сбор данных успешно завершен!!!")
