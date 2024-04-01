import random

def generate_random_sample(courses, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours):
    timetable = []
    for course in courses:
        course_scheduled = False  
        hours_needed = hours_per_course[course]
        for day in range(1, weekdays_num + 1):
            if course_scheduled:
                break 
            for room in rooms:
                if room_capacities[room] < students_per_course[course]:
                    continue
                for start_hour in range(1, max_lecture_hours + 1 - hours_needed):  
                    end_hour = start_hour + hours_needed
                    if is_time_slot_available(timetable, room, day, start_hour, end_hour):
                        timetable.append((course, room, day, start_hour, end_hour))
                        course_scheduled = True  
                        break  
                if course_scheduled:
                    break  
    return timetable


