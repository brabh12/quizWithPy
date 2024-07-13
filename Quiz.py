#quiz project

ques = [
    {
        "prompt": "What is the biggest country in africa",
        "options" : ["A. Algeria", "B. Egypt", "C. Tunisia", "D. Morocco"],
        "answer" : "A"
    },
    {
        "prompt": "Which country won the FIFA World Cup in 2018?",
        "options" : ["A. Brazil", "B. France", "C. Argentina", "D. Italie"],
        "answer" : "B"
    },
    {
        "prompt": "Which club has won the most UEFA Champions League titles?",
        "options" : ["A. Real Madird", "B. Barca", "C. Man City", "D. Man UTD"],
        "answer" : "A"
    },
    {
        "prompt": "Which club has won the most English FA Cup titles?",
        "options" : ["A. Barca", "B. Valencia", "C. Man City", "D. Arsenal"],
        "answer" : "D"
    }
]
def start_quiz(ques):
    name = input("write your name : ")
    score = 0
    for question in ques:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your Answer A,B,C,D ? : ").upper()
        if answer == question["answer"]:
            print(f"good job {name} correct answer!!")
            score += 1
        else:
            print(f"ammmm incorrect answer!!!! the correct answer was", question["answer"])

    print(f"you got {score} ")
    
start_quiz(ques)