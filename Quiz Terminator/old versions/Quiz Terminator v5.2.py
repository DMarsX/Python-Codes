from os import getcwd

print("\nLoading Rules and Dictionary...")

dictionary = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I"}

def generatePermutations():
    global filename
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
        
    print(str(len(output)) + " Permutations Generated\n")
    file = open(filepath+filename,"w")
    print('Saving "' + filename + '"...')
    file.write(temp)
    file.close()
    output = temp.split(",")
    print('"' + filename + '" is saved\n\n')
    return output


def same(solution,check):
    global quiz
    count = 0
    
    for j in range(len(solution)):
        if solution[j] == quiz[check][0][j]:
            count += 1
            
    if count == quiz[check][1]:
        return True


file = open("quiz.txt","r")
each = file.readline().strip().split(",")
questions = len(each)
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
        
print("Imported " + str(len(quiz)) + " Rules\n\n")


filepath = getcwd() + "\\Data\\"
filename = "permutations_" + "".join(str(num) for num in each) + ".txt"
try:
    file = open(filepath+filename,"r")
    print('"' + filename + '" found, importing...')
    output = file.readline()
    file.close()
    output = output.split(",")
    print(str(len(output)) + " Permutations imported\n\n")
    
except FileNotFoundError:
    print('Could not find "' + filename + '"\nGenerating New Permutations...')
    output = generatePermutations()


filename = filename.replace("permutations","output")
print("Analyzing...\n")
pending = []
for check in range(len(quiz)):
    print("Applying Rule: " + ",".join(str(used) for used in quiz[check]))
    for solution in output:
        if same(solution,check):
            pending.append(solution)

    output = pending
    pending = []
    if output == []:
        file = open(filename,"w")
        file.write('No Possible Solutions Were Found, Double Check The Rules In Your "quiz.txt"\n\n')
        file.write("Rules That Has Been Used (In Order):\n\n")
        for rule in range(check+1):
            file.write(",".join(str(used) for used in quiz[rule]) + "\n")
        file.close()
        import sys,webbrowser
        webbrowser.open(filename)
        sys.exit()
    print(str(len(output)) + " Permutations Left\n")


count = str(len(output))
print('\nAnalysis Complete: ' + count + ' Potential 10/10 Solutions\n\nOutputting to "' + filename + '"')

file = open(filename,"w")
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

output = "\n".join(output)
file.write(output)
file.write("\nCount: " + count)
file.close()  
print("Output Complete\n")

import webbrowser
webbrowser.open(filename)

input("Press Any Key To Exit...")
