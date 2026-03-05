def solution(new_id: str) -> str:
    s = new_id.lower()

    allowed = set("abcdefghijklmnopqrstuvwxyz0123456789-_.")
    s = "".join(ch for ch in s if ch in allowed)

    out = []
    prev_dot = False
    for ch in s:
        if ch == ".":
            if prev_dot:
                continue
            prev_dot = True
        else:
            prev_dot = False
        out.append(ch)
    s = "".join(out)

    s = s.strip(".")

    if not s:
        s = "a"

    s = s[:15].strip(".")

    while len(s) < 3:
        s += s[-1]

    return s