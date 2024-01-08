def getQuestionMarks(numberOfQuestionMarks):
    questionMarks = "(?"
    for questionMarkCounter in range(1, numberOfQuestionMarks):
        questionMarks += ", ?"
    return questionMarks + ")"