import requests
course_dict = {}


def list_courses():
    r = requests.get("https://hackbulgaria.com/api/students/")
    course_list = set()
    for k in r.json():
        for course in k["courses"]:
            course_list.add(course["name"])
    course_number = 0
    for course in course_list:
        course_number += 1
        course_dict[course_number] = course
    for course in course_dict:
        print("[{}] - {}".format(course, course_dict[course]))


def match_teams(course_id, team_size, group_time):
    r = requests.get("https://hackbulgaria.com/api/students/")
    student_list = []
    for k in r.json():
        for course in k["courses"]:
            if (course["name"] == course_dict[course_id]
            and course["group"] == group_time):
                student_list.append(k["name"])
    for team_start in range(0, len(student_list), team_size):
        print("==========")
        for team_step in range(0, team_size):
            if team_start + team_step < len(student_list):
                print(student_list[team_start + team_step])
            else:
                print("No more students!")



def main():
    print("Hello, you can use one the the following commands:\n",
    "list_courses - this lists all the courses that are available now.\n",
    "match_teams <course_id>, <team_size>, <group_time>\n")
    message = input()
    if message == "list_courses":
        list_courses()
    while message == "list_courses" or message.startswith("match_teams"):
        message = input()
        if message == "list_courses":
            list_courses()
        else:
            match = message.split(' ')
            match_teams(int(match[1]), int(match[2]), int(match[3]))

if __name__ == "__main__":
    main()
