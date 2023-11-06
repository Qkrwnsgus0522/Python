import matplotlib.pyplot as plt
import numpy as np
import csv

while True:
    with open('korea.csv', 'r') as file:
        data = csv.reader(file)
        header = next(data)                 # CSV 파일의 헤더를 읽어옵니다.

        area = input('동 이름 입력>> ')     # 사용자로부터 동 이름을 입력받습니다.

        found = False                       # 동 이름을 찾았는지 여부를 나타내는 변수
        dup = False                         # 중복된 동 이름이 있는지 여부를 나타내는 변수

        # CSV 파일을 한 줄씩 읽어가며 동 이름을 찾습니다.
        for row in data:
            if area in row[0]:              # 입력한 동 이름이 현재 행의 첫 번째 열(동 이름)에 있는지 확인합니다.
                if found:
                    dup = True              # 이미 동 이름을 찾았다면 중복으로 처리합니다.
                found = True                # 동 이름을 찾았음을 표시합니다.
                sample = np.array([int(value.replace(',', '')) for value in row[3:]], dtype=int)  # 데이터 추출
                print(row[0])               # 동 이름을 출력합니다.

        if dup:                             # 해당 이름을 가진 동이 여러개일 경우
            print('해당 이름을 가진 동이 여러개입니다!')
            print('정확하게 입력해주세요!')
        elif not found:                     # 해당 이름을 가진 동이 없을 경우
            print('해당 이름을 가진 동은 없습니다!')
            print('다시 입력하세요!')
        else:                               # 동 이름을 찾았거나 중복 없이 찾았을 경우
            plt.plot(sample)
            plt.show()
            break
