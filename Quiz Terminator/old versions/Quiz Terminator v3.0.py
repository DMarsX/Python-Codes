numberOfQuestions = 10
number_of_choices_for_each_question = [4,4,4,4,4,4,4,4,4,4]


file = open("quiz.txt","r")
quiz = file.readlines()
file.close()

for i in range(1,len(quiz)):
    j = i
    while quiz[j-1][-3] < quiz[j][-3] and j > 0:
        quiz[j-1],quiz[j] = quiz[j],quiz[j-1]
        j-=1

for i in range(len(quiz)):
    quiz[i] = quiz[i].strip().split(",")


def choices(List):
    
    x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    aList = []
    count = 0

    for number in List:
        aList.append(x[:number])
        count+=1

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


def String(Number):

    order = ["2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
    string = "index[-1]"
    for num in range(Number-1):
        string += "+index[-" + order[num] + "]"

    return string


def loop(string,Number,inverse):

    global count,index,output,y
    
    if Number == 0:
        z = eval(string)
        if same(z):
            output.append(z)
            count += 1

    else:
        for index[-Number] in y[inverse]:
            loop(string,Number-1,inverse+1)
            

print("\n↓Possible Solutions (Stops printing if exceeds 50, and opens a file at the end)\n")

a=b=c=d=e=f=g=h=i=j=k=l=m=n=o=p=q=r=s=t=u=v=w=0
index = [w,v,u,t,s,r,q,p,o,n,m,l,k,j,i,h,g,f,e,d,c,b,a]
count = 0

output = []
y = choices(number_of_choices_for_each_question)
string = String(numberOfQuestions)
loop(string,numberOfQuestions,0)


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
