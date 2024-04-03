import random
import math
import matplotlib.pyplot as plt
import copy

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
                for start_hour in range(1, max_lecture_hours - hours_needed + 1):
                    end_hour = start_hour + hours_needed
                    # 检查即使加上持续时间后，是否仍然不超过最大时间段
                    if end_hour  <= max_lecture_hours: 
                        if is_time_slot_available(timetable, room, day, start_hour, end_hour):
                            timetable.append((course, room, day, start_hour, end_hour))  # 使用 end_hour 无需加1
                            successfully_scheduled = True
                            break
    return timetable



def find_unused_time_slots(timetable, weekdays_num, max_lecture_hours):
    # 初始化每天的每个小时为未使用
    all_time_slots = {(day, hour): False for day in range(1, weekdays_num + 1) for hour in range(1, max_lecture_hours + 1)}

    # 标记使用的小时
    for _, _, day, start_hour, end_hour in timetable:
        for hour in range(start_hour, end_hour):
            all_time_slots[(day, hour)] = True

    # 查找连续的未使用小时，并创建时间段
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
        # 检查是否有跨越整天的未使用时间段
        if start is not None:
            unused_time_slots.append((day, start, max_lecture_hours + 1))

    return unused_time_slots







def mutate(timetable, courses, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours):
    mutated_timetable = copy.deepcopy(timetable)
    unused_time_slots = find_unused_time_slots(mutated_timetable, weekdays_num, max_lecture_hours)
    
    courses_to_mutate = random.sample(courses, k=random.randint(1, len(courses) // 2))
    
    for course in courses_to_mutate:
        mutated_timetable = [entry for entry in mutated_timetable if entry[0] != course]
        hours_needed = hours_per_course[course]

        shuffled_time_slots = unused_time_slots[:]  # 复制未使用时间段列表
        random.shuffle(shuffled_time_slots)  # 打乱时间段列表以增加随机性

        for _ in range(100):  # 尝试100次找到合适的时间段和教室
            day = random.randint(1, weekdays_num)
            room = random.choice(rooms)

            if room_capacities[room] >= students_per_course[course]:
                if shuffled_time_slots:  # 如果有未使用的时间段，优先考虑
                    slot = shuffled_time_slots.pop(0)  # 从打乱的列表中取出一个时间段
                    day, start, _ = slot  # 使用该时间段的起始时间
                else:
                    start = random.randint(1, max_lecture_hours - hours_needed + 1)  # 没有未使用时间段时随机选择开始时间
                
                end = start + hours_needed
                if end  <= max_lecture_hours and is_time_slot_available(mutated_timetable, room, day, start, end):
                    mutated_timetable.append((course, room, day, start, end))
                    break  # 成功安排后退出循环

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
