def match_parens(lst):
    s1, s2 = lst
    # Calculate the unbalanced left parentheses of String 1 and String 2
    left1, right1 = calc_unbalanced(s1)
    left2, right2 = calc_unbalanced(s2)
    # If the unbalanced right parentheses of String 1 are smaller than that of String 2, we should concatenate s1 with s2.
    # Otherwise, we should concatenate s2 with s1.
    if right1 <= left2 and left1 == right2:
        return 'Yes'
    elif right2 <= left1 and left2 == right1:
        return 'Yes'
    return 'No'


def calc_unbalanced(s):
    left = right = 0
    for c in s:
        if c == '(':  # If the parentheses is '('
            left += 1
        elif left > 0:  # If the parentheses is ')' and there is a unbalanced left parentheses
            left -= 1
        else:  # If the parentheses is ')' and there is no unbalanced left parentheses, count it as unbalanced right parentheses
            right += 1
    return left, right
