import random
class question:
    #Initializer
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer


    #instance
    def checkAnswer(self,answer):

        if answer not in self.choices:
            raise ValueError("[python","c#","java","dart] arasından bir cevap veriniz")
        return self.answer==answer

class Quiz:
    def __init__(self,questions):
        self.questions = random.sample(questions,len(questions))
        self.questionIndex=0
        self.score=0

    #instance quiz.questions dan soru almak
    def getQuestion(self):
        return self.questions[self.questionIndex]
    def displayQuestion(self):

        question=self.getQuestion()

        print(f"Soru {self.questionIndex + 1 }: {question.text}")

        for q in question.choices:
            print("-"+ q)

        answer =input('cevap: ')
        if(question.checkAnswer(answer)):
            self.score += 1
            print("bildiniz.")
        self.questionIndex+=1
        self.loadQuestion()
    def loadQuestion(self):
        if len(self.questions)==self.questionIndex:
            self.displayScore()

        else:
            self.displayProgress()
            self.displayQuestion()
    def displayScore(self):
        puan=100/ len(self.questions)
        toplamPuan = round(self.score*puan)
        print(f"toplam {len(self.questions)} sorunun {self.score} ını bildiniz . puanınız {toplamPuan}")
        print("score",self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber=self.questionIndex+ 1

        print(f"Toplam {totalQuestion} sorunun {questionNumber}.sorusundasınız.".center(100,'*'))


q1 = question("en iyi programlama dili hangisidir?",["python","c#","java","dart"],"python")
q2 = question("en popüler programlama dili hangisidir?",["python","java","c#","dart"],"python")
q3 = question("en çok kazandıran programlama dili hangisidir?",["python","java","dart","c#"],"python")

sorular = [q1,q2,q3]


quiz = Quiz(sorular)

print(quiz.loadQuestion())



