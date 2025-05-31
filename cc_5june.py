T = int(input())
for _ in range(T):
    N = int(input())
    X = [ int(j) for j in input().split() ]
    P = [ int(j) for j in input().split() ]

    final_answer_flag = 0


    # -->
    right_start = 0
    right_final = 0
    for i in range(N-1):
        if X[i] + P[i] >= X[i+1]:
            right_final = i+1
        else:
            break
    if right_final == N-1:
        print("YES")
        final_answer_flag = 1


    # ->->
    if final_answer_flag == 0:
        right_start = 0
        right_final = 0
        right_right_flag = 0
        multiple_start_flag = 0
        for i in range(N-1):
            if X[i] + P[i] >= X[i+1]:
                right_final = i+1
            else:
                if right_right_flag == 0:
                    right_start = i+1
                    right_final = i+1
                    right_right_flag = 1
                else:
                    multiple_start_flag = 1
                    break
        if multiple_start_flag == 0 and right_final == N-1:
            print("YES")

            final_answer_flag = 1


    # <--
    if final_answer_flag == 0:
        left_start = N-1
        left_final = N-1
        while(left_start):
            if X[left_start] - P[left_start] <= X[left_start-1]:
                left_final = left_start-1
                left_start -= 1
            else:
                break
        if left_final == 0:
            print("YES")
            final_answer_flag = 1


    # <-<-
    if final_answer_flag == 0:
        left_start = N-1
        left_final = N-1
        left_left_flag = 0
        multiple_start_flag = 0
        current = left_start
        while(current):
            if X[current] - P[current] <= X[current-1]:
                left_final = current-1
                current -= 1
            else:
                if left_left_flag == 0:
                    left_start = current - 1
                    left_final = current - 1
                    left_left_flag = 1
                    current -= 1
                else:
                    multiple_start_flag = 1
                    break
        if multiple_start_flag == 0 and left_final == 0:
            print("YES")
            final_answer_flag = 1


    # <-->
    if final_answer_flag == 0:
        # right_arrow_first
        right_start = 0
        right_final = 0
        for i in range(1,N-1):
            if X[i] + P[i] >= X[i+1]:
                right_final = i+1
            else:
                right_start = i+1
                right_final = i+1
        if right_final == N-1:
            # left arrow second
            left_start = right_start - 1
            left_final = left_start
            wrong_answer_flag = 0
            while(left_start):
                if X[left_start] - P[left_start] <= X[left_start-1]:
                    left_final = left_start - 1
                    left_start -= 1
                else:
                    wrong_answer_flag = 1
                    break
            if wrong_answer_flag == 0:
                print("YES")
                final_answer_flag = 1


    # -><-
    if final_answer_flag == 0:
        right_start = 0
        right_final = 0
        for i in range(N-1):
            if X[i] + P[i] >= X[i+1]:
                right_final = i+1
            else:
                break
        left_start = N-1
        left_final = N-1
        current = left_start
        while(current):
            if X[current] - P[current] <= X[current-1]:
                left_final = current - 1
                current -= 1
            else:
                break
        if right_final == left_final - 1:
            print("YES")
            final_answer_flag = 1

    if final_answer_flag == 0:
        print("NO")