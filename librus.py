# Create session (with support for messages, require the same password for Portal Librus and Synergia)  
from librus_tricks import create_session  
import librus_tricks
import info

from datetime import datetime

session = create_session(info.settings[0], info.settings[1])  

def GetLessons(day : int = 0):
    lessons = {}
    table = session.tomorrow_timetable.lessons if day == 1 else session.today_timetable.lessons
    for lesson in table:
        try:
            lessons[f'{lesson.start.strftime("%H:%M")}-{lesson.end.strftime("%H:%M")}'] = str(lesson.subject)
        except IndexError:
            pass

    return lessons

def GetGradesByTeacher(teacher):
    grades = {}
    for grade in filter(lambda g: str(teacher).lower() in str(g.teacher).lower(), session.grades()):
        try:
            grades[grade.grade] = grade.comments[0]
        except IndexError:
            pass

    return grades

def GetFreeDays():
    free = {}
    for msg in session.school_free_days():
        try:
            free[f'{msg.starts}-{msg.ends}'] = str(msg.name)
        except IndexError:
            pass

    return free

def GetMessages(teacher : str = '', limit : int = 5):
    messages = {}
    index = 0
    for msg in filter(lambda m: teacher.lower() in str(m.author).lower() and index < limit, session.message_reader.read_messages()):
        try:
            index += 1
            messages[msg.author] = str(msg.text)
        except Exception:
            pass

    return messages

def GetExams(subject : str = ''):
    exams = {}
    for ex in filter(lambda x: subject.lower() in str(x.subject).lower() and x.date >= datetime.now().date(), session.exams()):
        exams[f'[{ex.subject}] {ex.date}'] = f'{ex.content}'

    return exams