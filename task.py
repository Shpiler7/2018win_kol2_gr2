# class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) classes scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in classes
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

import json
import numpy as np

def showAllStudents(school):
	for student in school["student"]:
		stud_score = []
		stud_attendance = []
		all_attendance = 0
		print("{}. {} {}" . format(student["id"], student["name"], student["surname"]))
		if "classes" in student:
			print("\n\tClasses")
			for classes in student["classes"]:
				if "score" in classes:
					stud_score.extend(classes["score"])
				if "attendance" in classes:
					stud_attendance.extend(classes["attendance"])
					all_attendance = all_attendance + len(classes["attendance"])
				print("\t {}. {}" .format(classes["classes_id"], classes["classes_name"]))
				if "score" in classes:
					print("\t\t Scores: {}".format(classes["score"]))
					print("\t\t Average score: {:.2f}".format(np.mean(classes["score"])))
				if "attendance" in classes:
					print("\t\t Attendance: {}".format(classes["attendance"]))
					print("\t\t Total attendance: {}/{} {:.2f}%".format(sum(classes["attendance"]), len(classes["attendance"]), sum(classes["attendance"])/len(classes["attendance"])*100))
			if "score" in classes:	
				print("\n\tAverage score: {:.2f}".format(np.mean(stud_score)))
			if "attendance" in classes:
				print("\tTotal attendance {}/{} {:.2f}%\n".format(sum(stud_attendance), all_attendance, sum(stud_attendance)/all_attendance*100))
				
def addScore(school, stud_id, classes_id, score):
	for student in school["student"]:
		if student["id"] == int(stud_id):
			if "classes" in student:
				for classes in student["classes"]:
					if classes["classes_id"] == int(classes_id):
						if "score" not in classes:
							classes["score"] = []
						classes["score"].append(int(score))
						with open("school.json", mode='w') as f:
							json.dump(school, f)
						return "Score added!"
	return "No such student or classes"
	
def addAttendance(school, stud_id, classes_id, attendance):
	for student in school["student"]:
		if student["id"] == int(stud_id):
			if "classes" in student:
				for classes in student["classes"]:
					if classes["classes_id"] == int(classes_id):
						if "attendance" not in classes:
							classes["attendance"] = []
						classes["attendance"].append(int(attendance))
						with open("school.json", mode='w') as f:
							json.dump(school, f)
						return "Attendance added!"
	return "No such student or classes"
	
def addClass(school, stud_id, classes_name):
	for student in school["student"]:
		if student["id"] == int(stud_id):
			if "classes" not in student:
				student["classes"] = []
			if "classes" in student:
				student["classes"].append({"classes_id": len(student["classes"])+1, "classes_name": classes_name})
				with open("school.json", mode='w') as f:
					json.dump(school, f)
				return "Classes added!"
	return "No such student or classes"
	
def overallAverage(school):
	overallScore = []
	for student in school["student"]:
		if "classes" in student:
			for classes in student["classes"]:
				if "score" in classes:
					overallScore.extend(classes["score"])
	print("Overall average of all Students: {:.2f}".format(np.mean(overallScore)))
	
			

if __name__ == "__main__":
	school = json.load(open("school.json"))
	while True:
		print("\n*************************************")
		print("1 - Add student")
		print("2 - Show all students and their score")
		print("3 - Add student score")
		print("4 - Add attendance")
		print("5 - Add class to a student")
		print("q - Exit")
		print("*************************************\n")
		num = input()
		if num == "1":
			print("Name: ")
			name = input()
			print("Surname: ")
			surname = input()
			school["student"].append({"id": len(school["student"]) + 1, "name": name, "surname": surname})
			with open("school.json", mode='w') as f:
				json.dump(school, f)
		elif num == "2":
			showAllStudents(school)
			print("\n")
			overallAverage(school)
		elif num == "3":
			print("Choose student by id")
			stud_id = input()
			print("Choose classes by id")
			classes_id = input()
			print("Type score (1 to 5)")
			score = input()
			if (int(score) >= 1 and int(score) <= 5):
				print(addScore(school, stud_id, classes_id, score))
			else:
				print("Wrong input! Type 1 to 5.")
		elif num == "4":
			print("Choose student by id")
			stud_id = input()
			print("Choose classes by id")
			classes_id = input()
			print("Type attendance (0 or 1)")
			attendance = input()
			if (int(attendance) == 0 or int(attendance) == 1):
				print(addAttendance(school, stud_id, classes_id, attendance))
			else:
				print("Wrong input! Type 0 or 1.")
		elif num == "5":
			print("Choose student by id")
			stud_id = input()
			print("Type classes name")
			classes_name = input()
			print(addClass(school, stud_id, classes_name))
		elif num == "q":
			break
		else:
			print("Error")