import numpy as np

matrix = np.array(
    [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]
)

"""
equivalent of:
1s
2s 2p
3s 3p 3d 
4s 4p 4d 5f
5s 5p 4d 5f
6s 6p 6d
7s 7p
"""


def check_space(max_e):
    """Checks if there are enough electrons left to
    fill up any place on the current substrate."""

    for x in range(max_e, 0, -1):
        if zNumber - x >= 0:
            return x
    return False


def converter(value):
    return str(value).translate(symboltable)


zNumber = int(input("Enter the number of electrons: \n"))

if zNumber > 118:
    print("There is no known element with more than 118 electrons")
else:
    i_old, j_old = 0, 0
    i, j = 0, 0

    symboltable = str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹')
    result = ""
    while (zNumber + 1) != 0:

        # j represents the index on a row of the matrix ([i][j])
        if j == 0:
            if check_space(2):
                currElectrons = check_space(2)
                zNumber = zNumber - currElectrons
                matrix[i][j] = currElectrons
                result += str(i + 1) + "s" + converter(currElectrons) + " "
            else:
                break
        elif j == 1:
            if check_space(6):
                currElectrons = check_space(6)
                zNumber = zNumber - currElectrons
                matrix[i][j] = currElectrons
                result += str(i + 1) + "p" + converter(currElectrons) + " "
            else:
                break
        elif j == 2:
            if check_space(10):
                currElectrons = check_space(10)
                zNumber = zNumber - currElectrons
                matrix[i][j] = currElectrons

                # if there are 10 electrons on subshell d, you need 2 characters to form "10"
                if currElectrons > 9:
                    result += str(i + 1) + "d" + converter(round(currElectrons / 10)) + converter(round(currElectrons % 10)) + " "
                else:
                    result += str(i + 1) + "d" + converter(currElectrons) + " "
            else:
                break
        elif j == 3:
            if check_space(14):
                currElectrons = check_space(14)
                zNumber = zNumber - currElectrons
                matrix[i][j] = currElectrons
                if currElectrons > 9:
                    result = result + str(i + 1) + "f" + converter(round(currElectrons / 10)) + converter(round(currElectrons % 10)) + " "
                else:
                    result = result + str(i + 1) + "f" + converter(currElectrons) + " "
            else:
                break

        # selecting right indexes
        if j == 0:
            if i % 2 == 0:
                i = i_old
                i_old += 1
                j = j_old + 1
                j_old += 1
            elif i == 1:
                j = i + 1
                i -= 1
            elif i == 3:
                j = i
                i -= 2
            elif i == 5:
                j = i - 1
                i -= 3

        i += 1
        j -= 1

    print(result)
    input("Please enter any key to exit the program.")
