from random_timetable_generator import generate_random_sample
from simulated_annealing import simulated_annealing
from pso_optimizer import pso_optimize
# from genetic_algorithm_optimizer import genetic_algorithm_optimize
from utility_functions import calculate_conflict_occurrences,calculate_conflict_count,check_unassigned_courses,find_conflicting_courses,print_timetable_by_room,find_unused_time_slots1
from SEM1_lecture_and_rooms import weekdays_num, max_lecture_hours


def semster_lectures(courses, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours):
    #Generate initial schedule randomly
    
    print("Step 1: Generating Initial Timetable using Random Generation")
    initial_timetable= generate_random_sample(courses, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours)
    print_timetable_by_room(initial_timetable,hours_per_course)
    conflicts = calculate_conflict_occurrences(initial_timetable)  # Calculates conflicts based on room and start hour
    conflict_occurrences = calculate_conflict_count(initial_timetable) 
    print("conflict occurrences:", conflicts,"number of courses that conflict",conflict_occurrences)
    conflicting_courses = find_conflicting_courses(initial_timetable)
    print("Conflicting courses:", conflicting_courses)

    # Optimize random schedules using simulated annealing
    print("\nStep 2: Optimizing Timetable using Simulated Annealing")
    optimized_timetable = simulated_annealing(initial_timetable,courses, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num=5, max_lecture_hours=9, max_iterations=100000)
    print("Optimized class schedule and the number of conflicts：")
    print_timetable_by_room(optimized_timetable, hours_per_course)
    conflicts = calculate_conflict_occurrences(optimized_timetable)  # Calculates conflicts based on room and start hour
    conflict_occurrences = calculate_conflict_count(optimized_timetable) 
    print("conflict occurrences:", conflicts,"number of courses that conflict",conflict_occurrences)
    conflicting_courses = find_conflicting_courses(optimized_timetable)
    print("Conflicting courses:", conflicting_courses)
    unused_slots = find_unused_time_slots1(optimized_timetable, weekdays_num=5, max_lecture_hours=9)
    print("Unused Time Slots:")
    for slot in unused_slots:
    print(slot)

    # Optimize the results of simulated annealing using PSO
    print("\nStep 3: Further Optimizing Timetable using Particle Swarm Optimization (PSO)")
    final_timetable = pso_optimize(optimized_timetable,hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours, num_particles=30, max_iterations=10000, print_frequency=100)
    print("Optimized class schedule and the number of conflicts：")
    print_timetable_by_room(final_timetable, hours_per_course)
    conflicts = calculate_conflict_occurrences(final_timetable)  # Calculates conflicts based on room and start hour
    conflict_occurrences = calculate_conflict_count(final_timetable) 
    print("conflict occurrences:", conflicts,"number of courses that conflict",conflict_occurrences)
    conflicting_courses = find_conflicting_courses(final_timetable)
    print("Conflicting courses:", conflicting_courses)
    unused_slots = find_unused_time_slots1(final_timetable, weekdays_num=5, max_lecture_hours=9)
    print("Unused Time Slots:")
    for slot in unused_slots:
    print(slot)


    # Check unassigned courses
    unassigned = check_unassigned_courses(courses, final_timetable)
    if unassigned:
        print("Unassigned Courses after Optimization:", unassigned)
    else:
        print("All courses have been successfully scheduled.")


    print("We try to use Particle Swarm Optimization first and then use Simulated Annealing")
    
    
    # Optimize the results of simulated annealing using PSO
    print("\nStep 1:  using Particle Swarm Optimization (PSO)")
    pso_timetable = pso_optimize(initial_timetable,hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours, num_particles=30, max_iterations=10000, print_frequency=100)
    print("Optimized class schedule and the number of conflicts：")
    print_timetable_by_room(pso_timetable, hours_per_course)
    conflicts = calculate_conflict_occurrences(pso_timetable)  # Calculates conflicts based on room and start hour
    conflict_occurrences = calculate_conflict_count(pso_timetable) 
    print("conflict occurrences:", conflicts,"number of courses that conflict",conflict_occurrences)
    conflicting_courses = find_conflicting_courses(pso_timetable)
    print("Conflicting courses:", conflicting_courses)
    unused_slots = find_unused_time_slots1(pso_timetable, weekdays_num=5, max_lecture_hours=9)
    print("Unused Time Slots:")
    for slot in unused_slots:
    print(slot)
    
    # Optimize random schedules using simulated annealing
    print("\nStep 2: Optimizing Timetable using Simulated Annealing")
    SA_timetable = simulated_annealing(pso_timetable,courses, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num=5, max_lecture_hours=9, max_iterations=100000)
    print("Optimized class schedule and the number of conflicts：")
    print_timetable_by_room(SA_timetable, hours_per_course)
    conflicts = calculate_conflict_occurrences(SA_timetable)  # Calculates conflicts based on room and start hour
    conflict_occurrences = calculate_conflict_count(SA_timetable) 
    print("conflict occurrences:", conflicts,"number of courses that conflict",conflict_occurrences)
    conflicting_courses = find_conflicting_courses(SA_timetable)
    print("Conflicting courses:", conflicting_courses)
    unused_slots = find_unused_time_slots1(SA_timetable, weekdays_num=5, max_lecture_hours=9)
    print("Unused Time Slots:")
    for slot in unused_slots:
    print(slot)

    unassigned = check_unassigned_courses(courses, SA_timetable)
    if unassigned:
        print("Unassigned Courses after Optimization:", unassigned)
    else:
        print("All courses have been successfully scheduled.")


    print("Next consider about don't allocate courses on Wednesday afternoon, For this we only use simulated annealing to see what will happened")
    
    
    


