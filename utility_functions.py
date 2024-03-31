def get_unused_classrooms_count(timetable, rooms):
    used_rooms = {entry[1] for entry in timetable}
    unused_rooms_count = len(set(rooms) - used_rooms)
    return unused_rooms_count
    
def print_unused_classrooms(timetable, rooms):
    used_rooms = {entry[1] for entry in timetable}
    unused_rooms = set(rooms) - used_rooms
    print(f"Number of unused classrooms: {len(unused_rooms)}")
    if unused_rooms:
        print("The following classrooms were not used:")
        for room in unused_rooms:
            print(room)


def check_unassigned_courses(courses, optimized_timetable):
    assigned_courses = set(entry[0] for entry in optimized_timetable)
    unassigned_courses = set(courses) - assigned_courses
    return unassigned_courses

def calculate_conflicts(timetable):
    # Using the previous logic to calculate the number of conflicts individually
    time_slot_counts = {}
    for _, _, day, hour in timetable:
        if (day, hour) not in time_slot_counts:
            time_slot_counts[(day, hour)] = 1
        else:
            time_slot_counts[(day, hour)] += 1
    conflicts = sum(count > 1 for count in time_slot_counts.values())
    return conflicts

# def print_timetable(timetable, hours_per_course):
#     sorted_timetable = sorted(timetable, key=lambda x: (x[2], x[3]))  # Sort by day and hour
#     for entry in sorted_timetable:
#         course, room, day, hour = entry
#         duration = hours_per_course[course]
#         if duration == 1:
#             print(f"Course Code: {course}, Room Name: {room}, Day {day}, Hour {hour}")
#         elif duration == 2:
#             print(f"Course Code: {course}, Room Name: {room}, Day {day}, Hours {hour} and {hour + 1}")

# def print_timetable(initial_timetable, hours_per_course):
#     # Convert numeric hours to specific times
#     hour_conversion = {
#         1: "9 AM", 2: "10 AM", 3: "11 AM", 4: "12 PM", 5: "1 PM",
#         6: "2 PM", 7: "3 PM", 8: "4 PM", 9: "5 PM", 10: "6 PM"
#     }
#     # Convert numeric days to their names
#     day_conversion = {
#         1: "Monday", 2: "Tuesday", 3: "Wednesday",
#         4: "Thursday", 5: "Friday"
#     }
    
#     # Sort timetable by room, day, and hour
#     sorted_timetable = sorted(initial_timetable, key=lambda x: (x[1], x[2], x[3]))

#     current_room = ""
#     for entry in sorted_timetable:
#         room_name, day, hour = entry[1], entry[2], entry[3]
#         if room_name != current_room:
#             print(f"\n{room_name}:")
#             current_room = room_name
        
#         # Convert numeric day and hour using the dictionaries
#         day_str = day_conversion.get(day, "Invalid Day")
#         hour_str = hour_conversion.get(hour, "Invalid Hour")
        
#         print(f"  - Course Code: {entry[0]}, {day_str}, {hour_str}")

def print_timetable(initial_timetable, hours_per_course):
    # Convert numeric hours to specific times
    hour_conversion = {
        1: "9 AM", 2: "10 AM", 3: "11 AM", 4: "12 PM", 5: "1 PM",
        6: "2 PM", 7: "3 PM", 8: "4 PM", 9: "5 PM", 10: "6 PM"
    }
    # Convert numeric days to their names
    day_conversion = {
        1: "Monday", 2: "Tuesday", 3: "Wednesday",
        4: "Thursday", 5: "Friday"
    }
    
    # Sort timetable by course, room, day, and hour for better checking of continuous periods
    sorted_timetable = sorted(initial_timetable, key=lambda x: (x[0], x[1], x[2], x[3]))

    current_room = ""
    for i, entry in enumerate(sorted_timetable):
        course_code, room_name, day, start_hour = entry
        if room_name != current_room:
            print(f"\n{room_name}:")
            current_room = room_name
        
        # Initialize end_hour as start_hour
        end_hour = start_hour
        
        # Check for continuous periods for the same course
        while i + 1 < len(sorted_timetable) and \
              sorted_timetable[i + 1][0] == course_code and \
              sorted_timetable[i + 1][2] == day and \
              sorted_timetable[i + 1][3] == end_hour + 1:
            end_hour = sorted_timetable[i + 1][3]
            i += 1  # Move to the next entry

        # Convert numeric day and start_hour using the dictionaries
        day_str = day_conversion.get(day, "Invalid Day")
        start_hour_str = hour_conversion.get(start_hour, "Invalid Hour")
        
        if end_hour != start_hour:
            end_hour_str = hour_conversion.get(end_hour, "Invalid Hour")
            print(f"  - Course Code: {course_code}, {day_str}, {start_hour_str}-{end_hour_str}")
        else:
            print(f"  - Course Code: {course_code}, {day_str}, {start_hour_str}")
