import pytest
from sqlalchemy.orm import Session
from database import Student, SessionLocal, engine
import random


@pytest.fixture(scope="function")
def db_session():
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture
# Генерируем id user
def unique_user_id():
    return random.randint(100000, 999999)


# ТЕСТ 1: Добавление
def test_create_student(db_session: Session, unique_user_id: int):
    new_student = Student(
        user_id=unique_user_id,
        level="Elementary",
        education_form="personal",
        subject_id=1
    )

    db_session.add(new_student)
    db_session.commit()

    student_from_db = (db_session.query(Student).filter
                       (Student.user_id == unique_user_id).first())

    assert student_from_db is not None
    assert student_from_db.user_id == unique_user_id
    assert student_from_db.level == "Elementary"
    assert student_from_db.education_form == "personal"


# ТЕСТ 2: Редактирование
def test_edit_student(db_session: Session, unique_user_id: int):
    student_to_update = Student(
        user_id=unique_user_id,
        level="Beginner",
        education_form="group",
        subject_id=1
    )
    db_session.add(student_to_update)
    db_session.commit()

    (db_session.query(Student).filter(Student.user_id == unique_user_id).update({
        "level": "Pre-Intermediate"
    }))
    db_session.commit()

    updated_student = (db_session.query(Student).filter
                       (Student.user_id == unique_user_id).first())

    assert updated_student.level == "Pre-Intermediate"
    assert updated_student.education_form == "group"


# ТЕСТ 3: Удаление
def test_delete_student(db_session: Session, unique_user_id: int):
    student_to_delete = Student(
        user_id=unique_user_id,
        level="Advanced",
        education_form="personal",
        subject_id=1
    )
    db_session.add(student_to_delete)
    db_session.commit()

    student_before = (db_session.query(Student).filter
                      (Student.user_id == unique_user_id).first())
    assert student_before is not None

    (db_session.query(Student).filter
     (Student.user_id == unique_user_id).delete())
    db_session.commit()

    student_after = (db_session.query(Student).filter
                     (Student.user_id == unique_user_id).first())
    assert student_after is None
