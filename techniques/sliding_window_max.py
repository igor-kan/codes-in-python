from collections import deque
def sliding_window_max(a, k):
    dq = deque(); out = []
    for i, x in enumerate(a):
        while dq and a[dq[-1]] <= x: dq.pop()
        dq.append(i)
        if dq[0] <= i - k: dq.popleft()
        if i >= k - 1: out.append(a[dq[0]])
    return out

if __name__ == "__main__":
    assert sliding_window_max([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    print("ok")
