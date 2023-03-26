from question import Question

questions_prompt = [
    "What color are Apples?\n(a) Blue\n(b) Red\n(c) Black\n\n",
    "What color are Bananas?\n(a) Yellow\n(b) Red\n(c) Violet\n\n",
    "What color are Strawberry?\n(a) Blue\n(b) White\n(c) Red\n\n"
]

question = [
    Question(questions_prompt[0], "b"),
    Question(questions_prompt[1], "a"),
    Question(questions_prompt[2], "c")
]


def run_test(question):
    score = 0
    for i in question:
        answer = input(i.prompt)
        if answer == i.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions_prompt)) + " correct")


run_test(question)




