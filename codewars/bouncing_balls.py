def bouncing_ball(h, bounce, window):
    # invalid conditions
    if (h <= 0 or bounce <= 0 or bounce >= 1 or window >= h):
        return -1

    ans = 1
    my_h = h*bounce

    while (my_h > window):
        ans += 2
        my_h *= bounce

    return ans
