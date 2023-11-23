
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, select
from sqlalchemy.orm import relationship, declarative_base, Session

engine = create_engine('sqlite:///./questions.db')
Base = declarative_base()

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question = Column(String)
    answers = relationship("Answer", back_populates="question")

class Answer(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    answer = Column(String)
    is_correct = Column(Boolean)
    question_id = Column(Integer, ForeignKey('questions.id'))
    question = relationship("Question", back_populates="answers")

Base.metadata.create_all(engine)

with Session(engine) as session:
    # pyt = Question(
    #     question="На каком языке мы пишем бота?",
    # )
    # a1 = Answer(
    #     answer = "python",
    #     is_correct = True,
    #     question = Question(question="На каком языке мы пишем бота?")
    # )

    # session.add_all([a1])
    # session.commit()
    questions = select(Question)
    for question in session.scalars(questions):
        print(question.question)
        for answer in question.answers:
            print(answer.answer)
    