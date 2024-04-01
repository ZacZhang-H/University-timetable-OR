import copy
import random
import matplotlib.pyplot as plt
from utility_functions import calculate_conflicts, get_unused_classrooms_count


class Particle:
    def __init__(self, timetable, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours):
        self.position = copy.deepcopy(timetable)  # Deep copy to ensure independence
        self.velocity = [0 for _ in timetable]  # Initialize velocity
        self.best_position = copy.deepcopy(timetable)
        self.best_fitness = fitness(timetable, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours)

def update_velocity(particle, global_best_position, w, c1, c2, max_velocity=3):
    for i in range(len(particle.velocity)):
        cognitive_component = c1 * random.random() * (particle.best_position[i][3] - particle.position[i][3])
        social_component = c2 * random.random() * (global_best_position[i][3] - particle.position[i][3])
        velocity_change = w * particle.velocity[i] + cognitive_component + social_component
        particle.velocity[i] = max(-max_velocity, min(max_velocity, velocity_change))

def update_position(particle, weekdays_num, max_lecture_hours, hours_per_course, rooms):
    for i in range(len(particle.position)):
        course_code, room, day, start_hour, _ = particle.position[i]
        new_hour = int(round(start_hour + particle.velocity[i]))

        # Add random perturbation
        if random.random() < 0.2:
            new_hour += random.choice([-1, 1])

        new_hour = max(1, min(new_hour, max_lecture_hours))
        duration = hours_per_course[course_code]
        new_end_hour = new_hour + duration

        # Randomly change the room
        if random.random() < 0.2:
            room = random.choice(rooms)

        particle.position[i] = (course_code, room, day, new_hour, new_end_hour)


# PSO optimization remains largely the same, just pass hours_per_course to update_position

def pso_optimize(initial_timetable, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours, num_particles=30, max_iterations=10000, print_frequency=100):
    # Dynamically adjust the parameter w
    w_max = 0.9
    w_min = 0.4
    c1 = 2
    c2 = 5
    
    particles = [Particle(initial_timetable, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours) for _ in range(num_particles)]
    
    global_best_position = copy.deepcopy(initial_timetable)
    global_best_fitness = fitness(initial_timetable, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours)

    conflicts_history = []
    conflict_occurrences_history = []

    for iteration in range(max_iterations):
        # Dynamically adjust w
        w = w_max - (w_max - w_min) * (iteration / max_iterations)
        
        for particle in particles:
            update_velocity(particle, global_best_position, w, c1, c2)
            update_position(particle, weekdays_num, max_lecture_hours, hours_per_course, rooms)
            
            current_fitness = fitness(particle.position, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours)
            
            if current_fitness > particle.best_fitness:
                particle.best_position = copy.deepcopy(particle.position)
                particle.best_fitness = current_fitness
            
            if current_fitness > global_best_fitness:
                global_best_position = copy.deepcopy(particle.position)
                global_best_fitness = current_fitness

        # Record the current best solution's number of distinct conflicts and total conflict occurrences
        conflicts = calculate_conflict_count(global_best_position)
        conflict_occurrences = calculate_conflict_occurrences(global_best_position)
        conflicts_history.append(conflicts)
        conflict_occurrences_history.append(conflict_occurrences)

    # Plot the conflict history chart
    plt.figure(figsize=(10, 5))
    plt.plot(conflicts_history, label='Distinct Conflicts')
    plt.plot(conflict_occurrences_history, label='Total Conflict Occurrences')
    plt.xlabel('Iteration')
    plt.ylabel('Count')
    plt.title('PSO Optimization Process Visualization')
    plt.legend()
    plt.grid(True)
    plt.show()

    return global_best_position

