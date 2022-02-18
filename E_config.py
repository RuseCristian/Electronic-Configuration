import numpy as np

matrix = [[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]

matrix = np.array(matrix)
zNumberOriginal = int(input("enter the number of electrons: \n"))
zNumber = zNumberOriginal

i_old, j_old = 0, 0
i = 0
j = 0

def check_space(max_e):
    for x in range(max_e,0,-1):
        if zNumber - x >= 0:
            return x
    return False


symboltable=str.maketrans('0123456789','⁰¹²³⁴⁵⁶⁷⁸⁹')
def conv(string):
    return string.translate(symboltable)

result = ""
while (zNumber+1) != 0:
    if j == 0:
        if check_space(2):
            currElectrons = check_space(2) 
            zNumber = zNumber - currElectrons
            matrix[i][j] = currElectrons
            result = result + str(i+1)+"s"+conv(str(currElectrons)) + " "
        else:
            break
    elif j == 1:
        if check_space(6):
            currElectrons = check_space(6) 
            zNumber = zNumber - currElectrons
            matrix[i][j] = currElectrons
            result = result + str(i+1) + "p" + conv(str(currElectrons)) + " "
        else:
            break
    elif j == 2 :
        if check_space(10):
            currElectrons = check_space(10)
            zNumber = zNumber - currElectrons
            matrix[i][j] = currElectrons
            if currElectrons > 9:
                result = result + str(i+1) + "d" + conv(str(round(currElectrons/10))) + conv(str(round(currElectrons%10))) + " "
            else:
                result = result + str(i+1) + "d" + conv(str(currElectrons)) + " "
        else:
            break
    elif j == 3:
        if check_space(14):
            currElectrons = check_space(14) 
            zNumber = zNumber - currElectrons
            matrix[i][j] = currElectrons
            if currElectrons > 9:
                result = result + str(i+1) + "f" + conv(str(round(currElectrons/10))) + conv(str(round(currElectrons%10))) +" "
            else:
                result = result + str(i+1) + "f" + conv(str(currElectrons)) + " "
        else:
            break
            

    #selecting right index
    if j == 0 :
        if i % 2 == 0:
            i = i_old
            i_old += 1
            j = j_old + 1
            j_old += 1
        elif i == 1:
            j  = i + 1 
            i -= 1
        elif i == 3:
            j  = i
            i -= 2
        elif i == 5:
            j = i - 1
            i -= 3

    i += 1
    j -= 1


print(result)
input("pause")