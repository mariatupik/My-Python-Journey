import csv
from datetime import datetime, timedelta
def cheaters():
    time_begin = {}
    with open("start_times.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            name = line[0]
            start_time = line[1]
            time_begin[name] = datetime.strptime(start_time, "%H:%M")
    cheat = []
    with open("submissions.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            name = line[0]
            end_time = line[3]
            end_time = datetime.strptime(end_time, "%H:%M")
            if end_time - time_begin[name] > timedelta(hours=3):
                if name not in cheat:
                    cheat.append(name)
    
    return cheat

def final_points():
    time_begin = {}
    with open("start_times.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            name = line[0]
            start_time = line[1]
            time_begin[name] = datetime.strptime(start_time, "%H:%M")
    results = {}
    with open("submissions.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            name, task, points, sub_time = line
            task = int(task)
            points = int(points)
            end_time = datetime.strptime(sub_time, "%H:%M")
            if end_time - time_begin[name] <= timedelta(hours=3):
                if name not in results:
                    results[name] = {}
                if task not in results[name] or points > results[name][task]:
                    results[name][task] = points
    final_scores = {}
    for name, tasks in results.items():
        final_scores[name] = sum(tasks.values())
 
    return final_scores