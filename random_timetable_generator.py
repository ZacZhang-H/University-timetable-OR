import random
from utility_functions import calculate_conflict_occurrences,calculate_conflict_count,is_time_slot_available
def generate_random_sample(courses, hours_per_course, students_per_course, room_capacities, rooms, weekdays_num, max_lecture_hours):
    timetable = []
    for course in courses:
        course_scheduled = False
        hours_needed = hours_per_course[course]
        while not course_scheduled:
            day = random.randint(1, weekdays_num)
            room = random.choice(rooms)
            if room_capacities[room] >= students_per_course[course]:
                # 确保开始时间加上持续时间不会超过一天中的时间段
                if hours_needed == 1: # 如果课程只需要1小时
                    start_hour_range = max_lecture_hours  # 最后一个时间段可以使用
                else:
                    start_hour_range = max_lecture_hours - hours_needed + 1
                # 选择一个随机的开始时间
                start_hour = random.randint(1, start_hour_range)
                end_hour = start_hour + hours_needed
                if end_hour <= max_lecture_hours:  # 再次确认结束时间不会超出限制
                    if is_time_slot_available(timetable, room, day, start_hour, end_hour):
                        timetable.append((course, room, day, start_hour, end_hour))
                        course_scheduled = True
    return timetable


