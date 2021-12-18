from Storage_facility import Variables


class Attendance:
    def __init__(self, school_name, class_section):
        self.school = school_name
        self.cl = class_section        
        self.file = Variables(f"{school_name}-{class_section}")
        self.students = self.file.show_data().get('store',{})
        self.total_attendance = self.file.show_data().get('total', 0)

    def show_student_list(self):
        return sorted(list(self.students.keys()))

    def clear_student_list(self):
        self.students.clear()
        return True

    def take_attendance(self):
        for i in self.students.keys():
            self.students[i].append(input(f"Is {i} present? Y or X: ").upper())
        self.save()
        self.total_attendance += 1
        return True

    def add_new_student(self):
        student = input("Enter your new student's name: ")
        self.students[student] = list("X"*self.total_attendance)        
        return True
            

    def save(self):
        self.file.pass_all(
            total = self.total_attendance,
            school = self.school,
            class_section = self.cl,
            store = self.students,
            )
        self.file.save()
        return True
        
        
        
    
