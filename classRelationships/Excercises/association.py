class Instructor:
    def __init__(self, name: str):
        self.name = name
        self.courses = []

    def add_course(self, course):
        # TODO: Add course to list and set self as the course's instructor
        self.courses.append(course)
        course.set_instructor(self)
        pass

class Course:
    def __init__(self, title: str):
        self.title = title
        self.instructor = None
        self.students = []

    def set_instructor(self, instructor):
        # TODO: Set the instructor reference
        self.instructor = instructor
        

    def enroll_student(self, student):
        # TODO: Add student to list and set self as the student's enrolled course
        self.students.append(student)
        student.set_enrolled_course(self)
        

class Student:
    def __init__(self, name: str):
        self.name = name
        self.enrolled_course = None

    def set_enrolled_course(self, course):
        # TODO: Set the enrolled course reference
        self.enrolled_course = course

    def get_instructor_name(self) -> str:
        # TODO: Navigate through enrolled_course to get the instructor's name
        # Return "No instructor" if course or instructor is None
        if not self.enrolled_course:
            return 'No instructor'
        return self.enrolled_course.instructor.name

class Message:
    def __init__(self, author, content: str, timestamp: str):
        # TODO: Initialize fields
        self.author = author
        self.content = content
        self.timestamp = timestamp

class User:
    def __init__(self, name: str):
        self.name = name
        self.followers = []
        self.following = []
        self.messages = []

    def follow(self, user):
        # TODO: Add user to following, add self to user's followers
        # Guard against: self-follows, duplicates
        if user != self and self not in user.followers and user not in self.following:
            self.following.append(user)
            user.followers.append(self)

    def send_message(self, content: str, timestamp: str):
        # TODO: Create Message and add to messages list
        message = Message(self.name, content, timestamp)
        self.messages.append(message)

if __name__ == "__main__":
    alice = User("Alice")
    bob = User("Bob")
    charlie = User("Charlie")

    alice.follow(bob)
    alice.follow(charlie)
    bob.follow(alice)

    alice.send_message("Hello world!", "10:00 AM")
    bob.send_message("Learning OOP!", "10:30 AM")

    print(f"{alice.name} is following:")
    for u in alice.following:
        print(f"  - {u.name}")

    print(f"{bob.name}'s followers:")
    for u in bob.followers:
        print(f"  - {u.name}")

    print(f"{alice.name}'s messages:")
    for m in alice.messages:
        print(f"  [{m.timestamp}] {m.content}")

    alice = Instructor("Alice")
    dsa = Course("Data Structures")
    sys_design = Course("System Design")

    alice.add_course(dsa)
    alice.add_course(sys_design)

    bob = Student("Bob")
    charlie = Student("Charlie")

    dsa.enroll_student(bob)
    dsa.enroll_student(charlie)
    sys_design.enroll_student(charlie)

    print(f"{alice.name}'s courses:")
    for c in alice.courses:
        print(f"  - {c.title}")

    print(f"Students in {dsa.title}:")
    for s in dsa.students:
        print(f"  - {s.name}")

    print(f"{bob.name}'s instructor: {bob.get_instructor_name()}")