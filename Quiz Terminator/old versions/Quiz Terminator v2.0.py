file = open("quiz.txt","r")
quiz = file.readlines()
file.close()

for i in range(len(quiz)):
    quiz[i] = quiz[i].strip().split(",")


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


def same(z):

    global quiz

    count = [0]*len(quiz)
    
    for i in range(len(quiz)):
        for j in range(10):
            if z[j] == quiz[i][0][j]:
                count[i] += 1
                
    same = False
    for i in range(len(count)):
        if str(count[i]) == quiz[i][1]:
            same = True
        else:
            return False
    
    return same


print("\n↓Possible Solutions (Stops printing if exceeds 50, and opens a file at the end)\n")

output = []
y = choices(5,5,7,7,7,4,6,5,5,5)

count = 0
for a in y[0]:
    for b in y[1]:
        for c in y[2]:
            for d in y[3]:
                for e in y[4]:
                    for f in y[5]:
                        for g in y[6]:
                            for h in y[7]:
                                for i in y[8]:
                                    for j in y[9]:
                                        z = a+b+c+d+e+f+g+h+i+j
                                        if same(z):
                                            output.append(z)
                                            count += 1
                                            if count < 50:
                                                print(z)



file = open("output.txt","w")
file.write("Possible Soultions: \n\n")
for i in output:
    file.write(i+"\n")
file.write(str(count))
file.close()  
print("Count:",count,"\n")


for i in range(10):
    same = output[0][i]
    for j in range(len(output)):
        if output[j][i] != same:
            same = "Unknown"
            break
    print(str(i+1),same)

import webbrowser

webbrowser.open("output.txt")
