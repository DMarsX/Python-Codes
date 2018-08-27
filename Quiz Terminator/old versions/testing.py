file = open("quiz.txt","r")
quiz = file.readlines()
file.close()

for i in range(len(quiz)):
    quiz[i] = quiz[i].strip().split(",")
    quiz[i][1] = int(quiz[i][1])

for i in range(1,len(quiz)):
    j = i
    while quiz[j-1][1] < quiz[j][1] and j > 0:
        quiz[j-1],quiz[j] = quiz[j],quiz[j-1]
        j -= 1


def choices(a,b,c,d,e,f,g,h,i,j):
    
    x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    aList = [x[:a], #1
             x[:b], #2
             x[:c], #3
             x[:d], #4
             x[:e], #5
             x[:f], #6
             x[:g], #7
             x[:h], #8
             x[:i], #9
             x[:j]] #10

    return aList


def same(z,check):

    global quiz
    count = 0

    for j in range(len(z)):
        if z[j] == quiz[check][0][j]:
            count += 1

    if count == quiz[check][1]:
        return True


print("\n↓Possible Solutions (Stops printing if exceeds 50, and opens a file at the end)\n")

output = []
pending = []
y = choices(5,5,4,4,4,4,8,4,4,4)


for check in range(len(quiz)):
    for solution in output:
        if same(solution,check):
            pending.append(solution)
    output = pending[:]
    pending = []


file = open("output.txt","w")
file.write("Possible Soultions: \n\n")
for i in output:
    file.write(i+"\n")
file.write("Count: " + str(len(output)))
file.close()  
print("Found",len(output),"potential full mark answers.")

for i in range(10):
    same = output[0][i]
    for j in range(len(output)):
        if output[j][i] != same:
            same = "Unknown"
            break
    print(str(i+1),same)

import webbrowser

webbrowser.open("output.txt")

