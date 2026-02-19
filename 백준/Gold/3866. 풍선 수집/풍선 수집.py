import sys

def solve():
    while True:
        try:
            line = sys.stdin.readline()
            if not line: break
            n = int(line.strip())
            if n == 0: break
        except ValueError: break

        # 풍선 정보 입력 (위치, 시간)
        balloons = []
        for _ in range(n):
            p, t = map(int, sys.stdin.readline().split())
            balloons.append((p, t))
        
        # dp[i][j]: i번째 풍선을 잡았고, 현재 j개를 들고 있을 때의 최소 이동 거리
        # i는 0부터 n-1까지 (입력된 풍선 인덱스)
        # j는 1, 2, 3 (들고 있는 개수)
        # 초기값을 아주 큰 수로 설정
        inf = float('inf')
        dp = [[inf] * 4 for _ in range(n)]
        
        # 첫 번째 풍선 처리 (집 -> 1번 풍선)
        p1, t1 = balloons[0]
        dist = p1 # 집(0)에서 p1까지 거리
        time_needed = dist # 빈 손(0개)이므로 속도 1 => 시간 = 거리 * 1
        
        if time_needed <= t1:
            dp[0][1] = dist
        else:
            print(f"NG 1")
            continue

        fail_idx = -1
        
        # DP 수행
        for i in range(n - 1):
            curr_p, curr_t = balloons[i]
            next_p, next_t = balloons[i+1]
            dist_direct = abs(next_p - curr_p)
            dist_via_home = curr_p + next_p
            
            can_reach_next = False
            
            for j in range(1, 4): # 현재 들고 있는 풍선 개수 (1~3개)
                if dp[i][j] == inf: continue
                
                # Case 1: 바로 가기 (Go Direct)
                # 조건: 현재 j개 + 1개 <= 3
                if j + 1 <= 3:
                    time_cost = dist_direct * (j + 1) # 이동 속도는 (들고있는거 + 1)
                    if curr_t + time_cost <= next_t:
                        if dp[i][j] + dist_direct < dp[i+1][j+1]:
                            dp[i+1][j+1] = dp[i][j] + dist_direct
                            can_reach_next = True
                
                # Case 2: 집 들렀다 가기 (Via Home)
                # 집 갈 때는 j개 들고 감 -> 속도 j+1
                # 집에서 올 때는 0개 들고 옴 -> 속도 1
                time_cost = (curr_p * (j + 1)) + (next_p * 1)
                if curr_t + time_cost <= next_t:
                    if dp[i][j] + dist_via_home < dp[i+1][1]:
                        dp[i+1][1] = dp[i][j] + dist_via_home
                        can_reach_next = True
            
            # i번째에서 i+1번째로 가는 방법이 아예 없는 경우
            # 하지만 이미 앞 단계에서 걸러지지 않았는지 확인 필요.
            # 모든 j에 대해 dp[i+1][j]가 갱신되지 않았다면 실패
            is_possible = False
            for k in range(1, 4):
                if dp[i+1][k] != inf:
                    is_possible = True
                    break
            
            if not is_possible:
                fail_idx = i + 2 # i가 0부터 시작하므로 실제 번호는 i+1, 다음 풍선 못 잡으니 +1 더해서 i+2
                break
        
        if fail_idx != -1:
            print(f"NG {fail_idx}")
        else:
            # 마지막 풍선을 잡은 후 집으로 돌아와야 함
            ans = inf
            last_p = balloons[-1][0]
            for j in range(1, 4):
                if dp[n-1][j] != inf:
                    # 마지막 위치에서 집(0)까지 이동 거리만 더함
                    # (마지막 돌아오는 시간 제한은 문제에 명시되지 않음, "보관"이 목표이므로 거리만 추가)
                    ans = min(ans, dp[n-1][j] + last_p)
            
            if ans == inf:
                # 로직상 여기까지 오면 ans가 inf일 수 없으나 방어코드
                 print(f"NG {n}")
            else:
                print(f"OK {ans}")

solve()