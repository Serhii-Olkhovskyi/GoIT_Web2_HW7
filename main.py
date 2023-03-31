from sqlalchemy import func, desc
from src.models import Teacher, Student, Discipline, Grade, Group
from src.db import session

def select_1():
    """
    Знайти 5 студентів із найбільшим середнім балом з усіх предметів
    """
    r = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    return r


def select_2(discipline_id):
    """
    Знайти студента із найвищим середнім балом з певного предмета
    """
    r = session.query(Discipline.name, Student.fullname,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .filter(Discipline.id == discipline_id) \
        .group_by(Student.id, Discipline.name) \
        .order_by(desc('avg_grade')) \
        .limit(1).all()
    return r


def select_3(discipline_id):
    """
    Знайти середній бал у групах з певного предмета
    """
    r = session.query(Discipline.name, Group.name,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade) \
        .join(Student) \
        .join(Discipline) \
        .join(Group) \
        .filter(Discipline.id == discipline_id) \
        .group_by(Discipline.name) \
        .group_by(Group.name) \
        .order_by(desc('avg_grade'))\
        .all()
    return r


def select_4():
    """
    Знайти середній бал на потоці (по всій таблиці оцінок)
    """
    r = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade) \
        .all()
    return r

def select_5(teachers_id):
    """
    Знайти які курси читає певний викладач
    """
    r = session.query(Teacher.fullname, Discipline.name) \
        .select_from(Teacher) \
        .join(Discipline) \
        .filter(Teacher.id == teachers_id) \
        .group_by(Teacher.fullname) \
        .group_by(Discipline.name) \
        .all()
    return r


def select_6(group_id):
    """
    Знайти список студентів у певній групі
    """
    r = session.query(Group.name, Student.fullname) \
        .select_from(Student) \
        .join(Group) \
        .filter(Group.id == group_id) \
        .group_by(Student.fullname) \
        .group_by(Group.name) \
        .all()
    return r

def select_7(group_id, discipline_id):
    """
    Знайти оцінки студентів у окремій групі з певного предмета
    """
    r = session.query(Student.fullname, Grade.grade) \
        .select_from(Grade) \
        .join(Discipline) \
        .join(Student) \
        .join(Group) \
        .filter(Group.id == group_id) \
        .filter(Discipline.id == discipline_id) \
        .group_by(Student.fullname) \
        .group_by(Grade.grade) \
        .all()
    return r

def select_8(Teacher_id):
    """
    Знайти середній бал, який ставить певний викладач зі своїх предметів
    """
    r = session.query(Teacher.fullname, Discipline.name,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Teacher) \
        .join(Discipline) \
        .join(Grade) \
        .filter(Teacher.id == Teacher_id) \
        .group_by(Discipline.name) \
        .group_by(Teacher.fullname) \
        .order_by(desc('avg_grade')) \
        .all()
    return r


def select_9(student_id):
    """
    Знайти список курсів, які відвідує певний студент
    """
    r = session.query(Student.fullname, Discipline.name) \
        .select_from(Grade) \
        .join(Discipline) \
        .join(Student) \
        .filter(Student.id == student_id) \
        .group_by(Student.fullname) \
        .group_by(Discipline.name) \
        .all()
    return r

def select_10(student_id, teacher_id):
    """
    Список курсів, які певному студенту читає певний викладач
    """
    r = session.query(Student.fullname, Teacher.fullname, Discipline.name) \
        .select_from(Grade) \
        .join(Discipline) \
        .join(Student) \
        .join(Teacher) \
        .filter(Student.id == student_id) \
        .filter(Teacher.id == teacher_id) \
        .group_by(Student.fullname) \
        .group_by(Discipline.name) \
        .group_by(Teacher.fullname) \
        .all()
    return r


if __name__ == '__main__':
    print(f'5 студентів із найбільшим середнім балом з усіх предметів:\n {select_1()} \n')
    print(f'Cтудент із найвищим середнім балом з певного предмета:\n {select_2(1)} \n')
    print(f'Cередній бал у групах з певного предмета:\n {select_3(1)} \n')
    print(f'Cередній бал на потоці (по всій таблиці оцінок):\n {select_4()} \n')
    print(f'Які курси читає певний викладач:\n {select_5(1)} \n')
    print(f'Список студентів у певній групі:\n {select_6(1)} \n')
    print(f'Оцінки студентів у окремій групі з певного предмета:\n {select_7(1,1)} \n')
    print(f'Середній бал, який ставить певний викладач зі своїх предметів:\n {select_8(1)} \n')
    print(f'Список курсів, які відвідує певний студент:\n {select_9(1)} \n')
    print(f'Список курсів, які певному студенту читає певний викладач:\n {select_10(1,1)} \n')

