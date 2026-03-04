import urllib.request
import json
 
def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = my_request.read()
    courses = json.loads(data)
    
    active_courses = []
    for course in courses:
        if course['enabled']:
            course_tuple = (
                course['fullName'], 
                course['name'], 
                course['year'], 
                sum(course['exercises'])
            )
            active_courses.append(course_tuple)
            
    return active_courses
 
def retrieve_course(course_name: str):
    url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    my_request = urllib.request.urlopen(url)
    data = my_request.read()
    stats = json.loads(data)
    
    weeks_count = len(stats)
    max_students = 0
    total_hours = 0
    total_exercises = 0
    
    for week_data in stats.values():
        if week_data['students'] > max_students:
            max_students = week_data['students']
        
        total_hours += week_data['hour_total']
        total_exercises += week_data['exercise_total']
    
    result = {
        'weeks': weeks_count,
        'students': max_students,
        'hours': total_hours,
        'hours_average': total_hours // max_students,
        'exercises': total_exercises,
        'exercises_average': total_exercises // max_students
    }
    
    return result
 
if __name__ == "__main__":
    courses = retrieve_all()
    print(courses)
    print(retrieve_course("docker2019"))