#http://59.23.150.58/30stair/matti_block/matti_block.php?pname=matti_block
# 프로그램 명: matti_block
# 제한시간: 10 초
# 꼬마 매티는 블록놀이를 무척이나 좋아한다. 어느날 그는 아래 그림과 같은 모양으로 블록을 쌓았다.
# 그리고 매티는 그리는 것도 좋아한다. 매티는 블록을 다 쌓고 난 다음에는 그것을 보고 그림을 그리곤 한다. 3차원 상의 블록들의 모양을 그리는 것은 꼬마 매티에게는 상당히 어려운 작업이기 때문에 매티는 대신 블록들의 모양을 정면에서 바라본 그림과 오른쪽에 서 바라본 그림 둘을 그린다. 즉, 3차원 상에서 블록 빌딩의 모양을 정면과 오른쪽 측면 에서 바라본 투영체로써 그리는 것이다. 다음 그림은 위에 매티가 쌓은 블록 빌딩을 그 린 그림이다.
# 꼬마 매티는 이러한 두 가지의 그림이 있으면 다음에도 같은 모양의 블록 빌딩들을 쌓 을 수 있다고 믿었다.
#
# 몇 년후에 매티는 이 그림들을 다시 보게 되었는데,그림과 같은 블록 빌딩을 다시 쌓아 보려는 시도 중에 그 모양대로 쌓을 수 있는 블록 빌딩이 유일하 지 않다는 사실을 알게 되었다.계속적인 시도 결과 그는 단7개의 블록만 가지고 위의 그림과 같은 정면 모양과 오른쪽 측면 모양을 갖는 블록 빌딩을 재현해 낸 것은 물론 최 대 17개의 블록을 가지고도 그러한 블록 빌딩을 재현해 낼 수 있다는 사실을 알았다.
# 매티는 그가 어렸을 때, 그렸던 빌딩의 그림을 가지고 빌딩 블록을 재현해 보려고 한 다.빌딩 블록을 재현하는데 드는 최소의 블록 개수N과 최대의 블록 개수 M을 찾아내 는 프로그램을 작성하라. 제한시간은 10초이다.
#
# 입력
# 입력의
# 첫 행에는 블록 빌딩의 크기 K ( 1 <= K <= 1000 ) 가 주어진다. 블록 빌딩의 크기가 K 라는 것은 블록 빌딩의 가로, 세로, 높이의 길이가 블록을 K개 이어놓은 길이보다 같거나 작다는 것을 의미한다.
# 다음 줄에는 정면에서 바라본 그림의 모양을 나타내는 K 개의 정수가 사이에 한 칸의 공백을 두고 주어진다.각각의 정수는 정면에서 바라봤을 경우 왼쪽부터 차례대로 블록들의 높이를 나타내는 숫자로 0 이상 K 이하 의 수이다.
# 마찬가지로 다음 줄에는 오른쪽에서 바라본 그림의 모양을 나타내는 K개의 정수가 주어진다.
# 출력
# 첫 행에 블록 빌딩을 재현하는데 필요한 블록의 최소 개수 N 과 최대 개수 M 을 사이에 한 칸의 공백을 두고 출력한다.
# 입출력 예
# 입력
#
# 4
# 2 0 3 1
# 1 1 2 3
#
# 출력
#
# 7 17
# 출처:icu 영재 교육원
# 채점데이터:tncks0121(박수찬)
# [질/답] [제출 현황] [푼 후(1)]
# [ 채 점 ] [홈으로]  [뒤 로]

# input
# input_number = int(input())
# input_front_list_string = input().split()
# input_front_list = [int(a) for a in input_front_list_string]
# front_list = input_front_list[:]
# input_side_list_string = input().split()
# input_side_list = [int(a) for a in input_side_list_string]
# side_list = input_side_list[:]

# input
input_number = 3
input_front_list = [1, 1, 1]
front_list = input_front_list[:]
input_side_list = [1, 1, 1]
side_list = input_side_list[:]

# build front and side look
front_look = [[0 for j in range(input_number)] for i in range(input_number)]
side_look =  [[0 for j in range(input_number)] for i in range(input_number)]


# display front and side look
def print_look():
    i = 0
    while i < len(front_look):
        print(str(input_front_list[i]) + str(front_look[i]))
        i += 1
    print('')

    i = 0
    while i < len(side_look):
        print(str(input_side_list[i]) + str(side_look[i]))
        i += 1


# each floor maximum height calculation and remove 1 from two lists
def max_block_display_calculation():
    i = 0
    while i < len(front_list):
        j = 0
        while j < len(side_list):
            if front_list[i] >= 1 and side_list[j] >= 1:
                    front_look[i][j] += 1
                    side_look[j][len(side_list)-1-i] += 1
            j += 1
        i += 1

    i = 0
    while i < len(front_list):
        if front_list[i] >= 1:
            front_list[i] -= 1
        if side_list[i] >= 1:
            side_list[i] -= 1
        i += 1


# display result of loop for maximum height
while 1 in front_list and 1 in side_list:
    max_block_display_calculation()
    # print_look()
    # print(front_list, side_list)

# print maximum number of blocks
max_result = 0
for index_on_line in front_look:
    for front_look_i in index_on_line:
        max_result += front_look_i
# print("max_result ="+str(max_result))

print_look()


def min_block_location_calculation():
    front_look_i = 0
    while front_look_i < len(front_look):
        index_on_line = 0
        while index_on_line < len(front_look[front_look_i]):
            if front_look[front_look_i][index_on_line] == input_front_list[front_look_i] and \
                                front_look[front_look_i].count(input_front_list[front_look_i]) == 1:
                break
            side_look_i = 0
            while side_look_i < len(side_look):
                # if front_look_i == 0 and index_on_line == 2:
                    # print("debug")
                if front_look[front_look_i].count(input_front_list[front_look_i]) > 1 and \
                        front_look[front_look_i][index_on_line] == input_front_list[front_look_i] and \
                        side_look[index_on_line][len(side_look)-1-front_look_i] >= input_side_list[index_on_line]:
                    side_look_i += 1
                    continue
                if side_look[index_on_line].count(input_side_list[index_on_line]) == 1 and \
                        side_look[index_on_line][len(side_list) - 1 - front_look_i] == input_side_list[index_on_line]:
                    break
                else:
                    front_look[front_look_i][index_on_line] = 0
                    side_look[index_on_line][len(side_list) - 1 - front_look_i] = 0
                side_look_i += 1
            index_on_line += 1
        front_look_i += 1


# minimum
min_block_location_calculation()

# print minimum number of blocks
min_result = 0
for index_on_line in front_look:
    for front_look_i in index_on_line:
        min_result += front_look_i

# print_look()
print(min_result, max_result)

