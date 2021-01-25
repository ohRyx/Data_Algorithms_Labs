class Student:
    def __init__(self,name,studentNumber):
        # Remove pass and add your code here
        pass
      
    def addScore(self,subjectCode, examScore):
        # Remove pass and add your code here
        pass
      
    def getBestExamScore(self):
        # Remove pass and add your code here
        pass
      
    def getFailedModules(self):
        # Remove pass and add your code here
        pass
      
    def printScore(self):
        # Remove pass and add your code here
        pass

name = input("Enter student name:\n")
student_number = input("Enter student number:\n")
student = Student(name,student_number)

for i in range(5):
  subject_code = input("Enter subject code:\n")
  subject_score = int(input("Enter subject score:\n"))
  student.addScore(subject_code,subject_score)

print(student.name, student.studentNumber)
print("Best score =", student.getBestExamScore())
print("Failed modules =", student.getFailedModules())
print("Subject scores: ", student.printScore())