score_input = input("enter the score:").strip()
if not score_input:
    print("please enter a score")
else:

    score = float(score_input)
if not score.is_integer():
    print("score should be an integer")
elif score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score <= 89:
    print("B")
elif score >= 70 and score <= 79:
    print("C")
elif score >= 60 and score <= 69:
    print("D")
elif score >= 0 and score <= 59:
    print("F")
else:
    print("its not a valid score")
