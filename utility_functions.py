def is_time_slot_available(timetable, room, day, start_hour, end_hour):
    """
    Check if a given time slot is available in a specified room. Assumes the end hour is inclusive.

    Args:
    - timetable: The current timetable containing all course schedules.
    - room: The room to check for availability.
    - day: The day to check for availability.
    - start_hour: The starting hour of the time slot (inclusive).
    - end_hour: The ending hour of the time slot (inclusive).

    Returns:
    - True if the given time slot and room are free of conflicts.
    - False if there is a conflict.
    """
    for entry in timetable:
        _, entry_room, entry_day, entry_start_hour, entry_end_hour = entry
        # Check if it's the same room and day
        if room == entry_room and day == entry_day:
            # Check for time overlap, adjusted condition to include end hour
            if not (start_hour > entry_end_hour or end_hour < entry_start_hour):
                return False  # Time overlap found
    return True  # No time overlap found


def calculate_conflict_count(timetable):
    """
    Calculate the number of conflicts in the timetable.

    A conflict occurs when two or more courses are scheduled in the same time slot.

    Args:
    - timetable: The timetable to check for conflicts.

    Returns:
    - The count of conflicts in the timetable.
    """
    time_slots = {}
    for course, room, day, start_hour, _ in timetable:
        key = (day, start_hour)
        if key not in time_slots:
            time_slots[key] = set()
        time_slots[key].add(course)

    conflict_count = sum(len(courses) - 1 for courses in time_slots.values() if len(courses) > 1)
    return conflict_count


def calculate_conflict_occurrences(timetable):
    """
    Calculate the number of time slots in the timetable that have scheduling conflicts.

    A conflict is defined as two or more courses being scheduled at the same time and day.

    Args:
    - timetable: The timetable containing course scheduling information.

    Returns:
    - The number of time slots with conflicts.
    """
    time_slots = {}
    for course, room, day, start_hour, _ in timetable:
        key = (day, start_hour)
        if key not in time_slots:
            time_slots[key] = set()
        time_slots[key].add(course)

    conflict_occurrences = sum(len(courses) > 1 for courses in time_slots.values())
    return conflict_occurrences

def find_conflicting_courses(timetable):
    """
    Find and return a list of courses that have scheduling conflicts in the timetable.
    
    A conflict is defined as two or more courses being scheduled at the same time and day but in different rooms.

    Args:
    - timetable (list of tuples): The timetable containing course scheduling information. Each tuple consists of (course, room, day, start_hour, end_hour).

    Returns:
    - set: A set of conflicting courses.
    """
    conflicts = set()
    for index, (course, room, day, start_hour, end_hour) in enumerate(timetable):
        for other_course, other_room, other_day, other_start_hour, other_end_hour in timetable[index + 1:]:
            # Check if there is a time overlap but in different rooms
            if day == other_day and not (end_hour <= other_start_hour or start_hour >= other_end_hour) and room != other_room:
                conflicts.add(course)
                conflicts.add(other_course)

    return conflicts


def print_timetable_by_room(initial_timetable, hours_per_course):
    hour_conversion = {
        1: "9 AM", 2: "10 AM", 3: "11 AM", 4: "12 PM", 5: "1 PM",
        6: "2 PM", 7: "3 PM", 8: "4 PM", 9: "5 PM", 10: "6 PM"
    }
    day_conversion = {
        1: "Monday", 2: "Tuesday", 3: "Wednesday",
        4: "Thursday", 5: "Friday"
    }

    # Sort the timetable by room, day, and start hour
    sorted_timetable = sorted(initial_timetable, key=lambda x: (x[1], x[2], x[3]))

    current_room = ""

    for entry in sorted_timetable:
        course_code, room_name, day, start_hour, end_hour = entry

        if room_name != current_room:
            print(f"\n{room_name}:")
            current_room = room_name

        day_str = day_conversion.get(day, "Invalid Day")
        start_hour_str = hour_conversion.get(start_hour, "Invalid Hour")
        end_hour_str = hour_conversion.get(end_hour, "Invalid Hour")

        # Print the course details
        print(f"  - Course Code: {course_code}, {day_str}, {start_hour_str}-{end_hour_str}")


def check_unassigned_courses(courses, optimized_timetable):
    assigned_courses = set(entry[0] for entry in optimized_timetable)
    unassigned_courses = set(courses) - assigned_courses
    return unassigned_courses


def find_unused_time_slots1(timetable, weekdays_num, max_lecture_hours):
   
    all_time_slots = {(day, hour): False for day in range(1, weekdays_num + 1) for hour in range(1, max_lecture_hours + 1)}

    for _, _, day, start_hour, end_hour in timetable:
        for hour in range(start_hour, end_hour):
            all_time_slots[(day, hour)] = True

   
    unused_slots_list = [key for key, used in all_time_slots.items() if not used]

    hour_to_time = {1: "9am", 2: "10am", 3: "11am", 4: "12pm", 5: "1pm", 6: "2pm", 7: "3pm", 8: "4pm", 9: "5pm", 10: "6pm"}
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

  
    formatted_unused_slots = []
    for day, hour in sorted(unused_slots_list):
        day_name = day_names[day - 1]
        time_range = f"{hour_to_time[hour]} - {hour_to_time.get(hour+1, 'End of Day')}"
        formatted_unused_slots.append(f"{day_name}, {time_range}")

    return formatted_unused_slots
