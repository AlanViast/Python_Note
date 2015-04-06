#!/usr/bin/env python
' show a student  score grade  '


def getGrade(score) :
    """ get a score's grade """
    if 100 < score :
        return "Is not a standard score"
    elif 90 < score <= 100 :
        return "A"
    elif 80 < score <= 90 :
        return "B"
    elif 70 < score <= 80 :
        return "C"
    elif 60 < score <= 70 :
        return "D"
    else :
        return "E"


if __name__ == '__main__' :
    scoreStr = raw_input("Enter a student score > ")
    score = int(scoreStr)
    grade = getGrade(score)
    print grade
