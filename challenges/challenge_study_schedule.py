def study_schedule(permanence_period, target_time):
    if target_time is None or type(target_time) is not int:
        return None

    students_in_target_time = 0

    for student in permanence_period:
        start, finish = student
        if type(start) is not int or type(finish) is not int:
            return None
        elif start <= target_time <= finish:
            students_in_target_time += 1

    return students_in_target_time
