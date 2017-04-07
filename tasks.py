
tasks = {1:"TDD", 2:"OOP", 3:"Programming Logic", 4:"Version Control", 5:"Agile Methodology",
			6:"Growth Mindset", 7:"Asking Questions", 8:"Motivation and Commitment", 9:"Speaking"}

def mark_completed(l):
	t2 = tasks
	complete = []
	incomplete = []

	for i in l:
		if int(i) in t2.keys():
			complete.append(t2[int(i)])
			del(t2[int(i)])

	return [complete, t2.values()]

def run_app():

	inp = raw_input("Your name, Sir/Madam: ")
	print "\n"
	print "Welcome " + inp
	print "These are the tasks you are to complete."
	print "\n"

	for j, k in tasks.items():
		print str(j) + "." + k

	print "\n"

	l = list(raw_input("Enter Number(s) or press (ENTER) if none: "))
	ret = mark_completed(l)

	print "\n"

	print "Completed Tasks are: "
	print "**************************"
	for x in ret[0]:
		print x

	print "\n"

	print "Incompleted Tasks are: "
	print "**************************"
	for y in ret[1]:
		print y

	total = float(len(ret[0]) + len(ret[1]))
	complete = float(len(ret[0]))
	perc_complete = complete/total * 100
	
	print "\n"
	print "You have done " + str(int(complete)) + " out of " + str(int(total)) + " tasks."
	print "Progress at " + str(int(perc_complete)) + "%"

run_app()