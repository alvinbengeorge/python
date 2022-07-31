class DictionaryData:    
    def __init__(self):
        self.dictionary = {}
        
    def update_marks(self, new_marks, key):
        if key in self.dictionary:
            self.dictionary[key] = new_marks
            return "Success"
        return "This student doesnt exist. Please check the spelling"
        
    def remove_student(self, student_name):
        if student_name in self.dictionary:
            self.dictionary.pop(student_name)
            return "Success"
        return "This student doesnt exist"

    def add_marks(self, student_name, marks):
        if student_name not in self.dictionary:
            self.dictionary[student_name] = marks
            return "Success"
        return "This student already exists"
    
    def show_data(self, return_type = "string"):
        return_type = return_type.lower()
        if return_type == "string":
            all_keys = list(self.dictionary.keys())
            return "\n".join([f"{key}: {self.dictionary[key]}" for key in all_keys])
        else:
            return self.dictionary

Modes = """
You have three modes:

a) Add
b) Remove
c) Update
d) Show
e) Exit


"""

DD = DictionaryData()
student_name = None
marks = None

def input_marks():
    return [int(input(f"Enter {subject} mark: ")) for subject in ["Physics","Chemistry","Maths","Computer","English"]]

def get_student():
    return input("Enter student name: ")


while True:
    print(Modes)
    a = input("Enter mode:").lower()
    if a == "add":
        print(DD.add_marks(get_student(),input_marks()))
    if a == "show":
        print(DD.show_data())
    if a == "exit":
        print("Bye")
        break
    if a == "remove":
        print(DD.remove_student(get_student()))
    if a == "update":
        print(DD.update_marks(get_student(),input_marks()))

    print("-"*20)
        
        
        

    
