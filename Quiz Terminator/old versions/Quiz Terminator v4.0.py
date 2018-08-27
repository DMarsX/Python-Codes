print("\nLoading Rules and Dictionary...")

def same(solution,check):
    global quiz
    count = 0
    
    for j in range(len(solution)):
        if solution[j] == quiz[check][0][j]:
            count += 1
            
    if count == quiz[check][1]:
        return True


file = open("quiz.txt","r")
questions = int(file.readline().strip())
each = file.readline().strip().split(",")
quiz = file.readlines()
file.close()

for i in range(len(each)):
    each[i] = int(each[i])

for i in range(len(quiz)):
    quiz[i] = quiz[i].strip().split(",")
    quiz[i][1] = int(quiz[i][1])

for i in range(1,len(quiz)):
    j = i
    while quiz[j-1][1] < quiz[j][1] and j > 0:
        quiz[j-1],quiz[j] = quiz[j],quiz[j-1]
        j -= 1
        
print("Imported " + str(len(quiz)) + " Rules\n\nGenerating Permutations...")

dictionary = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I"}

output = [0]
pending = []
temp = []

for i in range(len(each)):
    for j in range(1,each[i]+1):
        pending.append(int(str(j)+"0"*(len(each)-i-1)))
    for item in output:
        for number in pending:
            temp.append(item + number)
    output = temp
    temp = []
    pending = []

temp = ",".join(str(num) for num in output)
for i in range(1,max(each)+1):
    temp = temp.replace(str(i),dictionary[i])
        
output = temp.split(",")
print(str(len(output)) + " Permutations Generated\n\n")

print("Analyzing...\n")
pending = []
for check in range(len(quiz)):
    for solution in output:
        if same(solution,check):
            pending.append(solution)

    output = pending
    pending = []
    if output == []:
        file = open("output.txt","w")
        file.write('No Possible Solutions Were Found, Double Check The Rules In Your "quiz.txt"\n\n')
        file.write("Rules That Has Been Used (In Order):\n\n")
        for rule in range(check+1):
            file.write(",".join(str(used) for used in quiz[rule]) + "\n")
        file.close()
        import sys,webbrowser
        webbrowser.open("output.txt")
        sys.exit()
    print("Rule Used: " + ",".join(str(used) for used in quiz[check]))
    print(str(len(output)) + " Permutations Left\n")


print("\nAnalysis Complete")
count = str(len(output))
file = open("output.txt","w")
file.write(count + " Possible Solutions Were Found (Potential Full Mark Answers)\n\n")

for i in range(questions):
    same = output[0][i]
    for j in range(int(count)):
        if output[j][i] != same:
            same = "Undetermined"
            break
    if i+1 < 10:
        file.write("Question " + str(i+1) + ":  " + same + "\n")
    else:
        file.write("Question " + str(i+1) + ": " + same + "\n")
file.write("\n\n↓ All Potential Solutions ↓\n\n")

for i in output:
    file.write(i+"\n")
file.write("Count: " + count)
file.close()  

import webbrowser
webbrowser.open("output.txt")
input()
