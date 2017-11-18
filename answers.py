
answers = {'hi':'hi there!', 'how are you':'fine, and you?', 'bye':'see you'}
def  get_answer(answers):
	question = input()
	return answers[question]
i=0
while i<5:
	a = get_answer(answers)
	print(a.lower())
	i+=1 