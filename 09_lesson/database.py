from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# Базовый класс для моделей
Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'

    user_id = Column(Integer, primary_key=True)
    level = Column(String)
    education_form = Column(String)
    subject_id = Column(Integer)

    def __repr__(self):
        return f"<Student(user_id={self.user_id}, level='{self.level}')>"


DATABASE_URL = "postgresql://postgres:12344321@localhost:5432/QA"

# "движок" для подключения к БД
engine = create_engine(DATABASE_URL)

# Фабрика сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
