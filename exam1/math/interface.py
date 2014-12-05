from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from expression import Expression
from sqlalchemy.sql import exists
from user import User
from connect import Base


def calculate_score(points):
    return points*points


def start(session):
    print("Dividing numbers rounds them to second decimal!")
    points = 0
    username = input("Enter your playername>")
    user = User(name=username, score=points)
    print("Welcome {}! Let the game begin!".format(username))
    last_answer_correct = True
    while(last_answer_correct):
        expression = Expression.generate_expression()
        print("What is the answer to {} {} {}".format(
            expression[0], expression[2], expression[1]))
        answer = input("?>")
        if(float(answer) == expression[3]):
            print("?>Correct!")
            points += 1
        else:
            score = calculate_score(points)
            print("Incorrect! Ending game. You score is: {}".format(score))
            last_answer_correct = False
            if user.score < score:
                user.score = score
                session.query(User).filter(User.name==username).update({"score": score})
    if(session.query(exists().where(User.name == username)).scalar() == 0):
        session.add(user)
    session.commit()


def highscores(session):
    print("This is the current top10:")
    high_scores = session.query(User).order_by(User.score.desc()).limit(10)
    for user in high_scores:
        print (user)


def begin(session):
    print('Welcome to the "Do you even math?" game!')
    print('Here are your options:')
    print('- start')
    print('- highscores')

    while True:
        command = input("?>")
        if command == "start":
            start(session)
        elif command == "highscores":
            highscores(session)


def main():
    engine = create_engine("sqlite:///game.db")
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    begin(session)


if __name__ == '__main__':
    main()