import copy
import sys

if len(sys.argv) < 2 :
    filename = "students.txt"
else:
    filename = sys.argv[1]

fr = open(filename,"r")
l = fr.readlines()
# 파일열고 한 줄 씩 읽기
read_list = []

for i in l:
    #line = fr.readline()
    read_list.append(i)

read_list

# 읽은 파일로부터 스플릿해주기 
s_list = []
for i in range(len(read_list)):
    s_list.append(read_list[i].strip().split("\t"))

print("student Name Midterm Final Average Grade")
print("-"*40)
for i in range(len(s_list)):
    print(*s_list[i])

# 학점이랑 평균 구하기 
for i in range(len(s_list)):
    avg=(int(s_list[i][2])+int(s_list[i][3]))/2
    if avg >=90:
        grade='A'
    elif avg >=80:
        grade='B'
    elif avg >=70:
        grade='C'
    elif avg >=60:
        grade='D'
    else:
        grade='F'
    
    s_list[i].append(avg)
    s_list[i].append(grade)
    
    
def show_function(input_list):
    
    # 딥카피 
    copy_input_list = copy.deepcopy(input_list)
    
    # 내림차순 정렬 
    sorted_input_list = sorted(copy_input_list, key=lambda e:e[4], reverse=True)
    
    # 보여주기 
    print("student Name Midterm Final Average Grade")
    print("-"*40)
    
    for elem_s_list in sorted_input_list:
        for j in range(len(elem_s_list)):
            print(elem_s_list[j], end=' ')
        print()
        
def search_function(s_list):
    
    SI=[]
    for i in range(len(s_list)):
        SI.append(s_list[i][0])
    
    search_id=input("Student ID: ")
    # 있으면은 인풋 값을 S_LIST 찾아야지
    # 인풋값에 해당되는 그 리스트 값을 출력할거야
    if search_id in SI:
        print("student Name Midterm Final Average Grade")
        print("-"*40)
        print(*s_list[SI.index(search_id)])
    # 그 값이 SI에 없으면 에러메시지를 출력할거야
    else:
        print("NO SUCH PERSON.")
        
def changescore_function(s_list):  
    student_id = input("Student ID: ")
    
    SI=[]
    
    for i in range(len(s_list)):
        SI.append(s_list[i][0])
    #student_id_index = SI.index(student_id)   
    # 학번이 목록에 있는지 확인
    if student_id in SI:
        student_id_index = SI.index(student_id)
        #있으면 중간이니 기말이니?
        exam = input("Mid/Final?: ")
        #만약 중간이거나 기말이면
        if exam == "mid" or exam == "final":
            #점수 입력
            n_score = int(input("Input new score: "))
            #점수가 0~100 사이이면
            if n_score>=0 and n_score<=100:
                #출력할거야
                
                print("student Name Midterm Final Average Grade")
                print("-"*40)
                print(*s_list[student_id_index])
                print("Score changed.")
                
                
            else:
                return
        #시험이 중간이면        
            if exam=='mid':
                s_list[student_id_index][2]=n_score
                avg=(n_score+int(s_list[student_id_index][3]))/2
                if avg >=90:
                    grade='A'
                elif avg >=80:
                    grade='B'
                elif avg >=70:
                    grade='C'
                elif avg >=60:
                    grade='D'
                else:
                    grade='F'
                s_list[student_id_index][4]=avg
                s_list[student_id_index][5]=grade
            else:
                s_list[student_id_index][3]=n_score
                avg=(n_score+int(s_list[student_id_index][2]))/2
                if avg >=90:
                    grade='A'
                elif avg >=80:
                    grade='B'
                elif avg >=70:
                    grade='C'
                elif avg >=60:
                    grade='D'
                else:
                    grade='F'
                
                s_list[student_id_index][4]=avg
                s_list[student_id_index][5]=grade
                
            print(*s_list[student_id_index])
            
        else:
            return 
    else:
        print("NO SUCH PERSON.")
        
def add_function(s_list):
    student_id = input("Student ID: ")
    ID=[]
    
    for i in range(len(s_list)):
        ID.append(s_list[i][0])
    if student_id in ID:
        print("ALREADY EXISTS.")
    
    else:
        name=input("Name: ")
        mid_s=input("midterm Score: ")
        fin_s=input("Final Score: ")
        print("Student added.")
        
        new=[]
        avg=(int(mid_s)+int(fin_s))/2
        if avg >=90:
            grade='A'
        elif avg >=80:
            grade='B'
        elif avg >=70:
            grade='C'
        elif avg >=60:
            grade='D'
        else:
            grade='F'
            
        for i in[student_id,name,mid_s,fin_s,avg,grade]:
            new.append(i)
            
        s_list.append(new)
        
def searchgrade_function(s_list):
    input_grade = input("Grade to search: ")
    grade_s=[]
    
    for i in range(len(s_list)):
        grade_s.append(s_list[i][5])
        
    grade_b=[]
    for i in range(len(grade_s)):
        if grade_s[i]==input_grade:
            grade_b.append(i)
            
    if input_grade in ['A','B','C','D','F']:
        if input_grade in grade_s:
            print("student Name Midterm Final Average Grade")
            print("-"*40)
            
            for i in grade_b:
                for j in range(len(s_list[i])):
                    print(s_list[i][j],end=' ')
                print()
                
        else:
            print("NO RESULT")
    else:
        return
    
def remove_function(s_list):
    if len(s_list) == 0:
        print("List is empty.")
        return
    
    remove_ID = input("Student ID: ")
    for i in range(len(s_list)):
        if s_list[i][0] == remove_ID:
            del s_list[i]
            print("Student removed.")
            return
    
    print("NO SUCH PERSON.")
    
    
def quit_function(s_list):
    data_input = input("Save data?[yes/no] ")
    
    if data_input == "yes":
        data_Filename = input("File name: ")
        copy_s_list = copy.deepcopy(s_list)
        sorted_s_list = sorted(copy_s_list, key=lambda e:e[4], reverse=True)
        with open(data_Filename, 'w') as f:
            for elem_s_list in sorted_s_list:
                f.write(elem_s_list[0]+'\t'+elem_s_list[1]+'\t'+str(elem_s_list[2])+'\t'+str(elem_s_list[3])+'\n')
    else:
        pass
    
stu_list = s_list

while True:
    command = input("# ").lower()
    if command == "show":
        show_function(stu_list)
    elif command == "search":
        search_function(stu_list)
    elif command =="changescore":
        changescore_function(stu_list)
    elif command == "add":
        add_function(stu_list)
    elif command == "searchgrade":
        searchgrade_function(stu_list)
    elif command == "remove":
        remove_function(stu_list)
    elif command == "quit":
        quit_function(stu_list)
        break
    else:
        continue
    