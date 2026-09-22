def closest_pair(points):
    best = float("inf"); pair = None
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2
            if d < best: best, pair = d, (points[i], points[j])
    return pair

if __name__ == "__main__":
    assert closest_pair([(0,0),(3,4),(1,1)]) == ((0,0),(1,1))
    print("ok")
