def collide(a, b):
    # a= (row, col), b= (row, col)

    return a[0] == b[0] or a[1] == b[1] or abs (a[0] - b[0]) == abs(a[1] - b[1])

def queens4():
    for q1 in range(4):
        for q2 in range(4):
            #Does placing a queen at (2, q2) collide with (1, q1)?
            if collide((1,q1), (2, q2)):
                continue
            for q3 in range(4):
                # Does placing a queen at (3, q3) collide with EITHER (1,q1) or (2,q2)?

                if collide((1, q1), (3, q3)) or collide((2, q2), (3, q3)):
                    continue
                for q4 in range(4):
                    if (collide((1, q1), (4, q4)) or collide((2, q2), (4, q4))
                        or collide((3, q3), (4, q4))):
                        continue
                    print(q1, q2, q3, q4)

queens4()
