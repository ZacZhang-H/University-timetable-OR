from Lectures import semster_lectures
from SEM1_lecture_and_rooms import courses1, hours_per_course1, students_per_course1, courses2, hours_per_course2, students_per_course2，room_capacities, rooms, weekdays_num, max_lecture_hours


def main():
  
  print("-------SEM1 Lecture-----")
  semster_lectures(courses1, hours_per_course1, students_per_course1, room_capacities, rooms, weekdays_num, max_lecture_hours)
  print("-------SEM2 Lecture-----")
  semster_lectures(courses2, hours_per_course2, students_per_course2, room_capacities, rooms, weekdays_num, max_lecture_hours)

if __name__ == "__main__":
    main()

