# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.
#If you can thing of any other features, you can add them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)


class  student(object):

	L = []

	def __init__(self, name, surname):
		self.name = name
		self.surname = surname

	def __str__(self):
		return self.name + " " + self.surname

	def averageScore(self):
		number = len(self.L)
		if number == 0:
			return "No scores"
		else:
			return sum(self.L)/number

	def addScore(self, score):
		self.L.append(score)


if __name__ == "__main__":
	studentsList = []
	while True:
		print("1 - Add student")
		print("2 - show all students")
		print("3 - add student score")
		print("4 - show student avg score")
		print("q - exit")
		num = input()
		if num == "1":
			print("Name: ")
			name = input()
			print("Surname: ")
			surname = input()
			studentsList.append(student(name, surname))
		elif num == "2":
			for i in studentsList:
				print(i)
		elif num == "3":
			l = len(studentsList)
			print("Choose student number: ")
			studnum = input()
			print("Type score: ")
			score = input()
			studentsList[int(studnum)].addScore(int(score))
		elif num == "4":
			l = len(studentsList)
			print("Choose student number: ")
			studnum = input()
			print(studentsList[int(studnum)].averageScore())
		elif num == "q":
			break
		else:
			print("Error")
