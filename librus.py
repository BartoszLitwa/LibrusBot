# Create session (with support for messages, require the same password for Portal Librus and Synergia)  
from librus_tricks import create_session  
import librus_tricks
import info
session = create_session(info.settings[0], info.settings[1])  

def GetLessons(teacher):
    lessons = ''
    for lesson in session.tomorrow_timetable.lessons:
        lessons.__add__(f'[{lesson.start.strftime("%H:%M")}-{lesson.end.strftime("%H:%M")}] {str(lesson.subject)}')

    return lessons

def GetGrades(teacher):
    grades = ''
    for grade in filter(lambda g: str(g.teacher) == teacher, session.grades()):
        grades.__add__(f'[{grade}] {grade.comments[0]}')

    return grades

#GetGrades()

def GetFreeDays():
    free = ''
    for msg in session.school_free_days():
        free.__add__(f'[{msg.starts}-{msg.ends}] {msg.name}')

    return free
