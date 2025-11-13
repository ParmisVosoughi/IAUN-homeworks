def custom_strip(s: str, chars: str | None = None) -> str:
    if not s:
        return s

    if chars is None:
        check = lambda ch: ch.isspace()
    else:
        chars_set = set(chars)
        check = lambda ch: ch in chars_set

    start = 0
    end = len(s) - 1

    while start <= end and check(s[start]):
        start += 1

    while end >= start and check(s[end]):
        end -= 1

    return s[start:end + 1]
