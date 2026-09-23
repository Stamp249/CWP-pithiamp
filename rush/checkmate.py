def checkmate(board):
    rows = board.strip().split("\n")

    # ตรวจสอบตาราง
    size = len(rows)

    if size == 0:
        return "Error"

    # ทุกแถวต้องยาวเท่ากัน และต้องเป็นตารางสี่เหลี่ยม
    if any(len(row) != size for row in rows):
        return "Error"

    # หา King
    kings = []

    for r in range(size):
        for c in range(size):
            if rows[r][c] == "K":
                kings.append((r, c))

    # ต้องมี King แค่ 1 ตัว
    if len(kings) != 1:
        return "Error"

    kr, kc = kings[0]

    # ทิศทางแนวตรง
    straight = [
        (-1, 0), (1, 0),
        (0, -1), (0, 1)
    ]

    # ทิศทางแนวทแยง
    diagonal = [
        (-1, -1), (-1, 1),
        (1, -1), (1, 1)
    ]

    # Rook / Queen
    for dr, dc in straight:
        r, c = kr + dr, kc + dc

        while 0 <= r < size and 0 <= c < size:
            piece = rows[r][c]

            if piece != ".":
                if piece == "R" or piece == "Q":
                    return "Success"
                break

            r += dr
            c += dc

    # Bishop / Queen
    for dr, dc in diagonal:
        r, c = kr + dr, kc + dc

        while 0 <= r < size and 0 <= c < size:
            piece = rows[r][c]

            if piece != ".":
                if piece == "B" or piece == "Q":
                    return "Success"
                break

            r += dr
            c += dc

    # Pawn
    for dc in (-1, 1):
        r = kr + 1
        c = kc + dc

        if 0 <= r < size and 0 <= c < size:
            if rows[r][c] == "P":
                return "Success"

    return "Fail"