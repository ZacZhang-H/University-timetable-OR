import copy
import random
import matplotlib.pyplot as plt
import math
from utility_functions import calculate_conflict_occurrences,calculate_conflict_count,is_time_slot_available
import numpy as np
from concurrent.futures import ThreadPoolExecutor

# def fitness(timetable, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours):
#     """
#     Calculate the fitness of a timetable, focusing on reducing the number of conflict occurrences and conflict count.
#     """
#     # Set a penalty for each conflict occurrence and each conflict count
#     conflict_penalty = 1000

#     # Calculate conflict occurrences and conflict counts
#     conflict_occurrences = calculate_conflict_occurrences(timetable)
#     conflict_count = calculate_conflict_count(timetable)
    
#     # Apply penalties for conflicts
#     total_penalty = (conflict_occurrences + conflict_count) * conflict_penalty

#     # The fitness is inversely proportional to the total penalty
#     fitness_score = -total_penalty

#     return fitness_score



# class Particle:
#     def __init__(self, timetable, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours):
#         self.position = copy.deepcopy(timetable)  # Deep copy to ensure independence
#         self.velocity = [0 for _ in timetable]  # Initialize velocity
#         self.best_position = copy.deepcopy(timetable)
#         self.best_fitness = fitness(timetable, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours)

# def update_velocity(particle, global_best_position, w, c1, c2, max_velocity=3):
#     for i in range(len(particle.velocity)):
#         cognitive_component = c1 * random.random() * (particle.best_position[i][3] - particle.position[i][3])
#         social_component = c2 * random.random() * (global_best_position[i][3] - particle.position[i][3])
#         velocity_change = w * particle.velocity[i] + cognitive_component + social_component
#         particle.velocity[i] = max(-max_velocity, min(max_velocity, velocity_change))

# def update_position(particle, weekdays_num, max_lecture_hours, hours_per_course, rooms):
#     for i in range(len(particle.position)):
#         course_code, room, day, start_hour, _ = particle.position[i]
#         hours_needed = hours_per_course[course_code]  #

       
#         new_start_hour = int(round(start_hour + particle.velocity[i]))

        
#         if random.random() < 0.2:
#             new_start_hour += random.choice([-1, 1])

        
#         new_start_hour = max(1, min(new_start_hour, max_lecture_hours - hours_needed + 1))

#         new_end_hour = new_start_hour + hours_needed  

        
#         if new_end_hour > max_lecture_hours:
#             new_end_hour = max_lecture_hours
#             new_start_hour = max(1, new_end_hour - hours_needed + 1)  

        
#         if random.random() < 0.2:
#             room = random.choice(rooms)

#         particle.position[i] = (course_code, room, day, new_start_hour, new_end_hour)

# # PSO optimization remains largely the same, just pass hours_per_course to update_position

# def pso_optimize(initial_timetable, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours, num_particles=30, max_iterations=10000, print_frequency=100):
#     # Dynamically adjust the parameter w
#     w_max = 0.9
#     w_min = 0.4
#     c1 = 2
#     c2 = 5
    
#     particles = [Particle(initial_timetable, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours) for _ in range(num_particles)]
    
#     global_best_position = copy.deepcopy(initial_timetable)
#     global_best_fitness = fitness(initial_timetable, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours)

#     conflicts_history = []
#     conflict_occurrences_history = []

#     for iteration in range(max_iterations):
#         # Dynamically adjust w
#         w = w_max - (w_max - w_min) * (iteration / max_iterations)
        
#         for particle in particles:
#             update_velocity(particle, global_best_position, w, c1, c2)
#             update_position(particle, weekdays_num, max_lecture_hours, hours_per_course, rooms)
            
#             current_fitness = fitness(particle.position, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours)
            
#             if current_fitness > particle.best_fitness:
#                 particle.best_position = copy.deepcopy(particle.position)
#                 particle.best_fitness = current_fitness
            
#             if current_fitness > global_best_fitness:
#                 global_best_position = copy.deepcopy(particle.position)
#                 global_best_fitness = current_fitness

#         # Record the current best solution's number of distinct conflicts and total conflict occurrences
#         conflicts = calculate_conflict_count(global_best_position)
#         conflict_occurrences = calculate_conflict_occurrences(global_best_position)
#         conflicts_history.append(conflicts)
#         conflict_occurrences_history.append(conflict_occurrences)

#     # Plot the conflict history chart
#     plt.figure(figsize=(10, 5))
#     plt.plot(conflicts_history, label='Distinct Conflicts')
#     plt.plot(conflict_occurrences_history, label='Total Conflict Occurrences')
#     plt.xlabel('Iteration')
#     plt.ylabel('Count')
#     plt.title('PSO Optimization Process Visualization')
#     plt.legend()
#     plt.grid(True)
#     plt.show()

#     return global_best_position

def fitness(timetable, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours):
    """
    Calculate the fitness of a timetable, focusing on reducing the number of conflict occurrences and conflict count.
    """
    # Set a penalty for each conflict occurrence and each conflict count
#     conflict_penalty = 1000

    # Calculate conflict occurrences and conflict counts
    conflict_occurrences = calculate_conflict_occurrences(timetable)
    conflict_count = calculate_conflict_count(timetable)
    
    # Apply penalties for conflicts
    total_penalty = (conflict_occurrences + conflict_count) 

    # The fitness is inversely proportional to the total penalty
    fitness_score = -total_penalty

    return fitness_score



class Particle:
    def __init__(self, timetable, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours):
        self.position = copy.deepcopy(timetable)  # Deep copy to ensure independence
        self.velocity = [0 for _ in timetable]  # Initialize velocity
        self.best_position = copy.deepcopy(timetable)
        self.best_fitness = fitness(timetable, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours)




def update_velocity(particle, global_best_position, w, c1, c2, max_velocity=5):
    for i in range(len(particle.velocity)):
        # Increase the impact of randomness
        cognitive_component = c1 * (0.5 + random.random()) * (particle.best_position[i][3] - particle.position[i][3])
        social_component = c2 * (0.5 + random.random()) * (global_best_position[i][3] - particle.position[i][3])
        velocity_change = w * particle.velocity[i] + cognitive_component + social_component
        particle.velocity[i] = max(-max_velocity, min(max_velocity, velocity_change))
def reinitialize_particle(particle, rooms, weekdays_num, max_lecture_hours, hours_per_course):
    if random.random() < 0.05:  # 5% chance to reinitialize the particle
        new_timetable = generate_sample(courses, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours)
        particle.position = copy.deepcopy(new_timetable)
        particle.velocity = [0 for _ in new_timetable]



def update_position(particle, weekdays_num, max_lecture_hours, hours_per_course, rooms, unused_time_slots):
    for i in range(len(particle.position)):
        course_code, room, day, start_hour, _ = particle.position[i]
        hours_needed = hours_per_course[course_code]

       
        if unused_time_slots:
            chosen_slot = random.choice(unused_time_slots)
            slot_day, start, end = chosen_slot
            
          
            if end - start >= hours_needed:
                new_start_hour = start
                new_end_hour = new_start_hour + hours_needed
              
                if new_end_hour <= max_lecture_hours:
                    particle.position[i] = (course_code, room, slot_day, new_start_hour, new_end_hour)
                    unused_time_slots.remove(chosen_slot)  
                    continue  

      
        new_start_hour = int(round(start_hour + particle.velocity[i]))
     
        new_start_hour = max(1, min(new_start_hour, max_lecture_hours - hours_needed + 1))
        new_end_hour = new_start_hour + hours_needed
       
        if new_end_hour > max_lecture_hours:
            new_end_hour = max_lecture_hours
            new_start_hour = max(1, new_end_hour - hours_needed)

        
        if random.random() < 0.9:
            room = random.choice(rooms)

        
        particle.position[i] = (course_code, room, day, new_start_hour, new_end_hour)






def find_unused_time_slots(timetable, weekdays_num, max_lecture_hours):

    all_time_slots = {(day, hour): False for day in range(1, weekdays_num + 1) for hour in range(1, max_lecture_hours + 1)}

 
    for _, _, day, start_hour, end_hour in timetable:
        for hour in range(start_hour, end_hour):
            all_time_slots[(day, hour)] = True

  
    unused_time_slots = []
    for day in range(1, weekdays_num + 1):
        start = None
        for hour in range(1, max_lecture_hours + 1):
            if all_time_slots[(day, hour)] == False:
                if start is None:
                    start = hour
            else:
                if start is not None:
                    unused_time_slots.append((day, start, hour))
                    start = None
     
        if start is not None:
            unused_time_slots.append((day, start, max_lecture_hours + 1))

    return unused_time_slots


def local_search(particle, hours_per_course, weekdays_num, max_lecture_hours):

    for i in range(len(particle.position)):
        course_code, room, day, start_hour, end_hour = particle.position[i]
        hours_needed = hours_per_course[course_code]

      
        if random.random() < 0.5:  
            new_start_hour = start_hour + random.choice([-1, 1])
            new_start_hour = max(1, min(new_start_hour, max_lecture_hours - hours_needed + 1))
            new_end_hour = new_start_hour + hours_needed

           
            if 1 <= new_start_hour <= max_lecture_hours and new_end_hour <= max_lecture_hours:
                particle.position[i] = (course_code, room, day, new_start_hour, new_end_hour)

def update_particle(particle, global_best_position, w, c1, c2, max_velocity, weekdays_num, max_lecture_hours, hours_per_course, rooms, unused_time_slots):
    update_velocity(particle, global_best_position, w, c1, c2, max_velocity)
    update_position(particle, weekdays_num, max_lecture_hours, hours_per_course, rooms, unused_time_slots)
    local_search(particle, hours_per_course, weekdays_num, max_lecture_hours)

def pso_optimize(initial_timetable, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours, num_particles=30, max_iterations=10000, print_frequency=100):
    w_max = 0.9
    w_min = 0.4
    c1 = 2
    c2 = 2
    max_velocity = 5

    particles = [Particle(initial_timetable, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours) for _ in range(num_particles)]
    global_best_position = copy.deepcopy(initial_timetable)
    global_best_fitness = fitness(initial_timetable, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours)

    conflicts_history = []
    conflict_occurrences_history = []

    with ThreadPoolExecutor() as executor:
        for iteration in range(max_iterations):
            w = w_max - (w_max - w_min) * (iteration / max_iterations)

            
            futures = [executor.submit(update_particle, particle, global_best_position, w, c1, c2, max_velocity, weekdays_num, max_lecture_hours, hours_per_course, rooms, find_unused_time_slots(particle.position, weekdays_num, max_lecture_hours)) for particle in particles]
            
            
            for future in futures:
                future.result()

           
            for particle in particles:
                current_fitness = fitness(particle.position, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours)
                if current_fitness > particle.best_fitness:
                    particle.best_position = copy.deepcopy(particle.position)
                    particle.best_fitness = current_fitness

                if current_fitness > global_best_fitness:
                    global_best_position = copy.deepcopy(particle.position)
                    global_best_fitness = current_fitness

            conflicts = calculate_conflict_count(global_best_position)
            conflict_occurrences = calculate_conflict_occurrences(global_best_position)
            conflicts_history.append(conflicts)
            conflict_occurrences_history.append(conflict_occurrences)


    plt.figure(figsize=(10, 5))
    plt.plot(conflicts_history, label='Distinct Conflicts')
    plt.plot(conflict_occurrences_history, label='Total Conflict Occurrences')
    plt.xlabel('times')
    plt.ylabel('number')
    plt.title('PSO Optimization Process Visualization')
    plt.legend()
    plt.grid(True)
    plt.show()

    return global_best_position
