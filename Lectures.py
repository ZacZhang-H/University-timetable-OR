from random_timetable_generator import generate_random_timetable
from simulated_annealing import simulated_annealing
from pso_optimizer import pso_optimize
from genetic_algorithm_optimizer import genetic_algorithm_optimize
from utility_functions import print_timetable, calculate_conflicts, check_unassigned_courses, print_unused_classrooms

def semster_lectures(courses, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours):
    #Generate initial schedule randomly
    print("-----------SEM1 lecture--------")
    print("Step 1: Generating Initial Timetable using Random Generation")
    initial_timetable = generate_random_timetable(courses, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours)
    print_timetable(initial_timetable, hours_per_course)
    print("Initial Conflicts:", calculate_conflicts(initial_timetable))
    print_unused_classrooms(initial_timetable, rooms)

    # Optimize random schedules using simulated annealing
    print("\nStep 2: Optimizing Timetable using Simulated Annealing")
    sa_optimized_timetable = simulated_annealing(initial_timetable,courses, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours, max_iterations=100000)
    print_timetable(sa_optimized_timetable, hours_per_course)
    print("SA Optimized Conflicts:", calculate_conflicts(sa_optimized_timetable))
    print_unused_classrooms(sa_optimized_timetable, rooms)

    # Optimize the results of simulated annealing using PSO
    print("\nStep 3: Further Optimizing Timetable using Particle Swarm Optimization (PSO)")
    pso_optimized_timetable = pso_optimize(sa_optimized_timetable, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours, num_particles=30, max_iterations=10000, print_frequency=100)
    print_timetable(pso_optimized_timetable, hours_per_course)
    print("PSO Optimized Conflicts:", calculate_conflicts(pso_optimized_timetable))
    print_unused_classrooms(pso_optimized_timetable, rooms)

    # Use genetic algorithm to optimize the results of PSO
    print("\nStep 4: Final Optimization using Genetic Algorithm (GA)")
    ga_optimized_timetable = genetic_algorithm_optimize(pso_optimized_timetable, hours_per_course, students_per_course, room_capacities, rooms, max_lecture_hours, population_size=1000, generations=200)
    print_timetable(ga_optimized_timetable, hours_per_course)
    print("GA Optimized Conflicts:", calculate_conflicts(ga_optimized_timetable))
    print_unused_classrooms(ga_optimized_timetable, rooms)

    # print("Step 1: Generating Initial Timetable using Random Generation")
    # initial_timetable = generate_random_timetable(courses, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours)
    # print_timetable(initial_timetable, hours_per_course)
    # print("Initial Conflicts:", calculate_conflicts(initial_timetable))
    # print_unused_classrooms(initial_timetable, rooms)

    # # Use genetic algorithm to optimize the results of PSO
    # print("\nStep 4: Final Optimization using Genetic Algorithm (GA)")
    # ga_optimized_timetable = genetic_algorithm_optimize(initial_timetable, hours_per_course, students_per_course, room_capacities, rooms, max_lecture_hours, population_size=1000, generations=200)
    # print_timetable(ga_optimized_timetable, hours_per_course)
    # print("GA Optimized Conflicts:", calculate_conflicts(ga_optimized_timetable))
    # print_unused_classrooms(ga_optimized_timetable, rooms)

    # # Optimize random schedules using simulated annealing
    # print("\nStep 2: Optimizing Timetable using Simulated Annealing")
    # sa_optimized_timetable = simulated_annealing(ga_optimized_timetable,courses, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours, max_iterations=100000)
    # print_timetable(sa_optimized_timetable, hours_per_course)
    # print("SA Optimized Conflicts:", calculate_conflicts(sa_optimized_timetable))
    # print_unused_classrooms(sa_optimized_timetable, rooms)

    # # Optimize the results of simulated annealing using PSO
    # print("\nStep 3: Further Optimizing Timetable using Particle Swarm Optimization (PSO)")
    # pso_optimized_timetable = pso_optimize(sa_optimized_timetable, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours, num_particles=30, max_iterations=10000, print_frequency=100)
    # print_timetable(pso_optimized_timetable, hours_per_course)
    # print("PSO Optimized Conflicts:", calculate_conflicts(pso_optimized_timetable))
    # print_unused_classrooms(pso_optimized_timetable, rooms)



    
    # Check unassigned courses
    unassigned = check_unassigned_courses(courses, ga_optimized_timetable)
    if unassigned:
        print("Unassigned Courses after Optimization:", unassigned)
    else:
        print("All courses have been successfully scheduled.")


