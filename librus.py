# Create session (with support for messages, require the same password for Portal Librus and Synergia)  
from librus_tricks import create_session  
import librus_tricks
import info
session = create_session(info.settings[0], info.settings[1])  

def GetLessons(teacher):
    lessons = []
    for lesson in session.tomorrow_timetable.lessons:
        try:
            lessons.append(f'[{lesson.start.strftime("%H:%M")}-{lesson.end.strftime("%H:%M")}] {str(lesson.subject)}')
        except IndexError:
            pass

    return lessons

def GetGrades(teacher):
    grades = []
    for grade in filter(lambda g: str(teacher).lower() in str(g.teacher).lower(), session.grades()):
        try:
            grades.append(f'[{grade.grade}] {grade.comments[0]}')
        except IndexError:
            pass

    return grades

def GetFreeDays():
    free = []
    for msg in session.school_free_days():
        try:
            free.append(f'[{msg.starts}-{msg.ends}] {msg.name}')
        except IndexError:
            pass

    return free