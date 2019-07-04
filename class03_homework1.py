class Course(): 
    def __init__(self, subject, code, credits, enrollment_classification, introduction, teacher, time):
        self.subject=subject
        self.code=code
        self.credits=credits
        self.enrollment_classification=enrollment_classification
        self.introduction=introduction
        self.teacher=teacher
        self.time=time

    def courseshow(self):
        print("科目",self.subject)
        print("課程編碼",self.code)
        print("學分",self.credits)
        print("必選修",self.enrollment_classification)
        print("課程簡介",self.introduction)
        print("老師",self.teacher)
        print("上課時間",self.time)

class Grade(Course):
    def __init__(self, subject, code, credits, enrollment_classification, introduction, teacher, time, grade):
        super().__init__(subject, code, credits, enrollment_classification, introduction, teacher, time)
        self.grade=grade   

    def gradeshow(self):
        Course.courseshow(self)
        print("成績",self.grade)

class People():
    def __init__(self, name, number):
        self.name=name
        self.number=number
    
    def peopleshow(self):
        print("姓名",self.name)
        print("學號",self.number)

class Student(People):
    def __init__(self, name, number, subject_list, grade_list):
        super().__init__(name, number)
        self.subject_list=subject_list
        self.grade_list=grade_list
        
    def setGrade(self):
        for num in range(len(self.subject_list)):
            self.subject_list[num] =Grade(self.subject_list[num].subject,self.subject_list[num].code,self.subject_list[num].credits,self.subject_list[num].enrollment_classification,self.subject_list[num].introduction,self.subject_list[num].teacher,self.subject_list[num].time,self.grade_list[num])        
    
        return self.subject_list
    
    def studentshow(self):
        People.peopleshow(self)
        self.setGrade()
        for s in self.subject_list:
            s.gradeshow()
            print("----------------")
        self.avgGrade()

    def avgGrade(self):
        sum = 0
        avg_sum = 0
        avg = 0
        for num_1 in range(len(self.subject_list)):
            sum += self.subject_list[num_1].credits
            avg_sum += self.subject_list[num_1].credits*self.grade_list[num_1]
            avg = avg_sum/sum

        print("總學分： ", sum)
        print("加權平均：", avg) 
            
special_topics_study=Course("專題研究(二)", "COME492", 1, "必修", "專題討論", "陳益生", "(六)12:10-13:00")
web_programming=Course("Web程式設計", "IECS272", 3, "選修", "教導學生開發Responsive Web應用程式的知識與能力", "陳錫民", "(二)10:10-12:00 (四)17:10-18:00")
the_shih_chi=Course("史記", "CHIN205", 2, "選修", "研讀史記", "楊美美", "(四)13:10-15:00")
japanese=Course("日文(一)", "LC101", 2, "選修", "從日語的五十音教起，配合選定教材，讓同學活用於日常會話之中。", "林盈萱", "(三)15:10-17:00")
korean=Course("韓文(二) ", "LC124", 2, "選修", "本課程希望透過韓文，增進同學對韓國的社會變遷與生活環境有深刻的瞭解。", "韓連善", "(三)13:10-15:00")
cryptography=Course("密碼學", "IECS352", 3, "選修", "概述密碼學及其相關應用的基礎知識", "魏國瑞", "(三)18:10-21:00")
electromagnetics=Course("電磁學(二) ", "COME21", 3, "必修", "學習Maxwell's Equation", "林漢年", "(二) 10:10~12:00 (四)08:10~09:00")
introduction_Compatibility=Course("電磁相容導論", "COME413", 3, "選修", "學習EMI和EMS", "彭嘉美", "(四) 08:10~12:00")
experiments_Compatibility=Course("電磁相容實習 ", "COME414", 1, "選修", "量測電磁干擾", "林漢年", "(三) 13:10~16:00")
microwave_Cricuit_Analysis=Course("微波電路分析", "COME634", 2, "選修", "本課程主要在講授微波電路，內容涵蓋阻抗匹配、低雜訊放大器、功率放大器、混頻器等。", "何滿龍", "(四) 14:10~17:00")

for i in [special_topics_study,web_programming,the_shih_chi,japanese,korean,cryptography,electromagnetics,introduction_Compatibility,experiments_Compatibility,microwave_Cricuit_Analysis]:
    i.courseshow()
    print("==================================")

print()

subject1=[special_topics_study,web_programming,the_shih_chi,japanese,korean]

grade1=[91,75,82,87,88]

student1=Student("張三", "D0448495",subject1,grade1)
student1.studentshow()

print("\n"+"******************************************")

subject2=[special_topics_study,web_programming,the_shih_chi,japanese,cryptography]

grade2=[91,78,80,86,80]

student2=Student("李四", "D0448185",subject2,grade2)
student2.studentshow()

print("\n"+"******************************************")

subject3=[electromagnetics,introduction_Compatibility,experiments_Compatibility,microwave_Cricuit_Analysis]

grade3=[90,80,95,87]

student3=Student("王五", "D0411111",subject3,grade3)
student3.studentshow()