import matplotlib.pyplot as plt
import numpy as np
import csv

while True:
    with open('korea.csv', 'r') as file:
        data = csv.reader(file)
        header = next(data)
        area = input('동 이름 입력>> ')

        found = False
        dup = False

        for row in data:
            if area in row[0]:
                if found:
                    dup = True
                found = True
                sample = np.array([int(value.replace(',', '')) for value in row[3:]], dtype=int)
                print(row[0])

        if dup:
            print('해당 이름을 가진 동이 여러개입니다!')
            print('정확하게 입력해주세요!')
        elif not found:
            print('해당 이름을 가진 동은 없습니다!')
            print('다시 입력하세요!')
        else:
            plt.plot(sample)
            plt.show()
            break
