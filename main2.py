from turtle import * # font=('Helvetica', 16, 'italic')
Screen().setup(width=1280, height=720)
Screen().bgpic('c:/Users/1/Downloads/5079b134-9e71-4e96-a7d8-b8b4fc377f0e.png')
hideturtle()
penup()
x, y = -500, 200 #начальная позиция
goto(x, y)


sentences = []

while True:
	count_sentences = int(input('Введите количество предложений : '))
	if count_sentences <= 28:
		break
	else:
		print('Превышает количество предложений (макс 28)')
 
for i in range(count_sentences):
	while True:
		sentence = input('Введите текст, макс 49 символов : ')
		if len(sentence) <= 49:
			sentences.append(sentence)
			break
		else:
			print('Превышает количество символов, введите текст заново : ')

for sent in sentences:
	for word in sent:
		write(word, font=('Helvetica', 12, 'italic'))
		forward(15)
	y -= 20
	goto(x, y)
	
	


done()