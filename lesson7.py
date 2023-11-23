
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, select
from sqlalchemy.orm import relationship, declarative_base, Session

engine = create_engine('sqlite:///./questions_new.db')
Base = declarative_base()

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    alternative = Column(String)


Base.metadata.create_all(engine)


with Session(engine) as session:
    q1 = Question(
        question="На каком языке мы пишем бота?",
        answer="python",
        alternative="C++, English, Telegram"
    )

    q2 = Question(
        question="Какую библиотеку мы используем для написания бота?",
        answer="python-telegram-bot",
        alternative="aiogram, pyrogram, telethone"
    )

    # session.add_all([q1, q2])
    # session.commit()

    questions = select(Question)
    for question in session.scalars(questions):
        print(question.question, question.answer, question.alternative)
