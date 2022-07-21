def look_and_tell(n):
    if n == 1:
        return "1"
    if n == 2:
        return "11"
    str_ = "11"
    for i in range(3, n + 1):
        str_ += " "
        length = len(str_)
        count = 1
        temp = ""
        for j in range(1, length):
            if str_[j] != str_[j - 1]:
                temp += str(count + 0)
                temp += str_[j - 1]
                count = 1
            else:
                count += 1
        str_ = temp
    return str_
