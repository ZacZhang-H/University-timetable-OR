import random
import math
import matplotlib.pyplot as plt

from utility_functions import calculate_conflict_occurrences,calculate_conflict_count,is_time_slot_available

random.seed(43)

def fitness(timetable, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours):
    """
    Calculate the fitness of a timetable, focusing on reducing the number of conflict occurrences and conflict count.
    """
    # Set a penalty for each conflict occurrence and each conflict count
    conflict_penalty = 1000

    # Calculate conflict occurrences and conflict counts
    conflict_occurrences = calculate_conflict_occurrences(timetable)
    conflict_count = calculate_conflict_count(timetable)
    
    # Apply penalties for conflicts
    total_penalty = (conflict_occurrences + conflict_count) * conflict_penalty

    # The fitness is inversely proportional to the total penalty
    fitness_score = -total_penalty

    return fitness_score



def generate_sample(courses, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours):
    """
    Generates a sample timetable considering continuous time requirements and avoiding duplicate scheduling.

    Args:
    - courses: A list of courses to schedule.
    - hours_per_course: A dictionary mapping each course to its duration in hours.
    - students_per_course: A dictionary mapping each course to its number of students.
    - room_capacities: A dictionary mapping each room to its capacity.
    - rooms: A list of available rooms.
    - weekdays_num: The number of weekdays available for scheduling.
    - max_lecture_hours: The maximum number of lecture hours in a day.

    Returns:
    - A list of tuples representing the timetable. Each tuple consists of (course, room, day, start_hour, end_hour).
    """
    timetable = []
    for course in courses:
        hours_needed = hours_per_course[course]
        successfully_scheduled = False
        for day in range(1, weekdays_num + 1):
            if successfully_scheduled:
                break
            for room in rooms:
                if room_capacities[room] < students_per_course[course]:
                    continue
                for start_hour in range(1, max_lecture_hours + 1):
                    end_hour = start_hour + hours_needed
                    if end_hour <= max_lecture_hours + 1 and is_time_slot_available(timetable, room, day, start_hour, end_hour):
                        timetable.append((course, room, day, start_hour, end_hour))
                        successfully_scheduled = True
                        break
    return timetable


def mutate(timetable, courses, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours):
    """
    Mutates the timetable based on the given parameters, ensuring no time overlaps or duplicate scheduling.

    Args:
    - timetable: The current timetable to mutate.
    - courses: A list of courses to potentially mutate.
    - hours_per_course: A dictionary mapping each course to its duration in hours.
    - students_per_course: A dictionary mapping each course to its number of students.
    - room_capacities: A dictionary mapping each room to its capacity.
    - rooms: A list of available rooms.
    - weekdays_num: The number of weekdays available for scheduling.
    - max_lecture_hours: The maximum number of lecture hours in a day.

    Returns:
    - A mutated timetable with potentially different scheduling for some courses.
    """
    mutated_timetable = copy.deepcopy(timetable)
    
    # Randomly select the number of courses to mutate
    num_courses_to_mutate = random.randint(1, len(courses) // 2)
    courses_to_mutate = random.sample(courses, num_courses_to_mutate)
    
    for course_to_mutate in courses_to_mutate:
        hours_needed = hours_per_course[course_to_mutate]
        
        # Randomly select a new time and location
        new_day = random.randint(1, weekdays_num)
        new_start_hour = random.randint(1, max_lecture_hours - hours_needed + 1)
        new_end_hour = new_start_hour + hours_needed
        new_room = random.choice(rooms)
        
        # Check if the new time and location are available and make updates
        if is_time_slot_available(mutated_timetable, new_room, new_day, new_start_hour, new_end_hour):
            # Remove all current scheduling for this course
            mutated_timetable = [entry for entry in mutated_timetable if entry[0] != course_to_mutate]
            # Add the new scheduling
            mutated_timetable.append((course_to_mutate, new_room, new_day, new_start_hour, new_end_hour))
    
    return mutated_timetable








    
    return mutated_timetable
def simulated_annealing(timetable, courses, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours, max_iterations=100000):
    """Simulated annealing process to optimize the timetable."""
    initial_temp = 10000
    final_temp = 0.0001
    alpha = 0.92
    current_temp = initial_temp

    conflicts_history = []  # For distinct conflict counts
    conflict_occurrences_history = []  # For total number of conflict occurrences

    current_solution = timetable
    current_fitness = fitness(current_solution, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours)
    best_solution = current_solution
    best_fitness = current_fitness

    iteration = 0
    while current_temp > final_temp and iteration < max_iterations:
        new_solution = mutate(current_solution, courses, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours)

        new_fitness = fitness(new_solution, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours)

        if new_fitness > current_fitness or random.random() < math.exp((new_fitness - current_fitness) / current_temp):
            current_solution = new_solution
            current_fitness = new_fitness
            if current_fitness > best_fitness:
                best_solution = current_solution
                best_fitness = current_fitness

        current_temp *= alpha
        iteration += 1

        # Update both conflict counts and occurrences
        conflicts_times = calculate_conflict_count(best_solution)
        total_conflicts = calculate_conflict_occurrences(best_solution) 

        conflicts_history.append(conflicts_times)
        conflict_occurrences_history.append(total_conflicts)

    # Plot
    plt.figure(figsize=(10, 5))
    plt.plot(conflicts_history, label='Distinct Conflicts')
    plt.plot(conflict_occurrences_history, label='Total Conflict Occurrences')
    plt.xlabel('Iteration')
    plt.ylabel('Count')
    plt.title('Optimization Process Visualization')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return best_solution

