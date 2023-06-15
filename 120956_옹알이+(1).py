def solution(babbling):
    # babbling -> 외부로부터 주어짐
    # babbling <= 단어들이 요소들로 묶여져 있는 형태
    # 묶여져있다 -> 발음을 할 수 있는지 '검사'해야한다
    pron = ["aya", "ye", "woo", "ma"]
    answer = 0  # 답을 주면 되겠구나 -> 발음 여부
    for b in babbling:  # 검사하고 싶은 단어들의 리스트 -> 단어(요소) b
        print(f"원래 b : {b}")
        # b -> pron을 돌아가면서 '제거'해주면... => 발음할 수 없는 것만 남는다
        # 제거를 했는데 b의 길이가 0 초과면? => 이 조합으로 발음할 수 없는...
        for p in pron:
            # b = b.replace(p, "")
            b = b.replace(p, "*")
        print(f"제거 b : {b}")  # wyeoo -> ppron의 순서에 따라서 먼저 ye가 제거가 되면, woo -> 발음?
        b = b.replace("*", "")
        if len(b) == 0:
            answer += 1
    return answer