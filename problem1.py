#gradebook program that processes student grades#
def get_grade():
    list=[]
    print("enter the grade of 5 students:")
    for i in range(5):
        try:
           grade=int(input(f"grade {i+1} "))
           if 0 <= grade <= 100:
              list.append(grade)
           else:
            print("inavalid grade, the grade must be between 0 and 100")
        except ValueError:
           print("inavalid input.please enter an valid grade")
        ''' The get_grade() function doesn't return the list of grades. It only prints them and appends them to the global list variable.'''
    return list 
def grade_category(grade):
    try :
        if 90<= grade <=100 :
          return 'A'
        elif 80<= grade <=89:
          return 'B'
        elif 70<= grade <=79:
          return 'C'
        elif 60<= grade <=69:
          return 'D'
        elif grade<=60:
          return 'E'
        else:
           print("inavalid grade")
    except ValueError:
       print("Inavalid Grade.") 
def process_grades(grades):
    for i, grade in enumerate(grades):
      category=grade_category(grade)
      print(f" student{i+1} grade {grade} corresponding score {category}")   
def summary_statistics(grades):
   highest_grade =max(grades)
   lowest_grade =min(grades)
   avregae =sum(grades)/len(grades)
   count_A= count_B= count_C= count_D= count_E= count_F=0
   ''' grades is a list, but grade_category() expects a single grade (not a list).'''
   for i in grades:
    category=grade_category(i)
    if  category == 'A':
         count_A+=1
    elif  category == 'B':
         count_B+=1
    elif  category == 'c':
         count_C+=1
    elif  category == 'D':
         count_D+=1
    elif  category == 'E':
         count_E+=1
    else:
         count_F+=1
   print(f"the highest {highest_grade}")
   print(f"the lowest: {lowest_grade}")
   print(f"the average: {avregae}")
   print(f"the number of A's :{count_A}")
   print(f"the number of B's :{count_B}")
   print(f"the number of C's :{count_C}")
   print(f"the number of D's :{count_D}")
   print(f"the number of F's :{count_F}")
   print(f"the number of E's :{count_E}")
def main(): 
  grades=get_grade()
  process_grades(grades)
  summary_statistics(grades)
main()
