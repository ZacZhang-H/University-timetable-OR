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

def print_timetable(timetable, hours_per_course):

    sorted_timetable = sorted(initial_timetable, key=lambda x: (x[1], x[2], x[3]))

    current_room = ""
    for entry in sorted_timetable:
        room_name = entry[1]
        if room_name != current_room:
            print(f"\n{room_name}:")
            current_room = room_name
       
        hour_str = f"Hour {entry[3]}" 
        print(f"  - Course Code: {entry[0]}, Day {entry[2]}, {hour_str}")
