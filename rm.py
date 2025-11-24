def read_marks():
    marks = []
    n = int(input("Enter number of students: "))
    for i in range(n):
        mark = float(input(f"Enter mark for student {i+1}: "))
        marks.append(mark)
    return marks