students = []
scores = []
for _ in range(int(input())):
        name = input()
        score = float(input())

        scores.append(score)
        students.append([name, score])

setted_scores = list(set(scores))
setted_scores.sort()
students.sort()


for i in range(len(students)):
        if students[i][1] == setted_scores[1]:
                print(students[i][0])