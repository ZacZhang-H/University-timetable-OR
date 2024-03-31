import random

def generate_random_timetable(courses, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours):
    timetable = []  # Initialize an empty list to store the timetable entries
    assigned_courses = set()  # A set to track the courses that have been allocated to prevent duplication

    # Iterate over each course to schedule it
    for course in courses:
        if course in assigned_courses:
            # Skip the course if it has already been allocated
            continue

        hours_needed = hours_per_course[course]  # Get the number of hours needed for the course
        
        # List of rooms that can accommodate the number of students in the course
        suitable_rooms = [room for room in rooms if room_capacities.get(room, 0) >= students_per_course.get(course, 0)]
        
        # Check if there are no suitable rooms and raise an error if true
        if not suitable_rooms:
            raise ValueError(f"No suitable room found for course '{course}' with {students_per_course[course]} students")

        # Schedule each hour needed for the course
        for _ in range(hours_needed):
            room = random.choice(suitable_rooms)  # Randomly choose a suitable room
            day = random.randint(1, weekdays_num)  # Randomly choose a day
            hour = random.randint(1, max_lecture_hours)  # Randomly choose an hour

            # Check if the chosen time slot is already occupied and find a new one if it is
            while any((existing_course[1], existing_course[2], existing_course[3]) == (room, day, hour) for existing_course in timetable):
                day = random.randint(1, weekdays_num)
                hour = random.randint(1, max_lecture_hours)

            # Add the scheduled course to the timetable
            timetable.append((course, room, day, hour))
        
        assigned_courses.add(course)  # Mark the course as allocated

    return timetable  # Return the completed timetable
