def dfs_8_puzzle(start, goal):
    """
    DFS giải bài toán 8-puzzle (khung 3x3)
    start, goal: dạng tuple (ví dụ: (1, 2, 3, 4, 5, 6, 7, 8, 0))
    """

    def get_neighbors(state):
        neighbors = []
        # Tìm vị trí của số 0 (ô trống) trong mảng phẳng
        idx = state.index(0)
        # Chuyển chỉ số từ mảng phẳng (0-8) sang tọa độ 2D (hàng x, cột y)
        x, y = divmod(idx, 3) 

        # 4 hướng di chuyển: Lên, Xuống, Trái, Phải
        moves = [(-1,0), (1,0), (0,-1), (0,1)]

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            # Kiểm tra xem vị trí mới có nằm trong khung 3x3 không
            if 0 <= nx < 3 and 0 <= ny < 3:
                # Chuyển tọa độ 2D ngược lại thành chỉ số mảng 1D
                new_idx = nx * 3 + ny
                # Chuyển tuple sang list để có thể hoán đổi vị trí (vì tuple không sửa được)
                new_state = list(state)
                # Hoán đổi ô trống (0) với số ở vị trí mới
                new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
                # Lưu trạng thái mới dưới dạng tuple để đưa vào set 'visited'
                neighbors.append(tuple(new_state))
        return neighbors

    # Khởi tạo Stack (Ngăn xếp) cho DFS - LIFO (Vào sau ra trước)
    stack = [start]
    # Tập hợp các trạng thái đã kiểm tra để tránh lặp vô hạn
    visited = set([start])
    # Từ điển lưu vết: parent[trạng thái mới] = trạng thái trước đó
    parent = {}

    while stack:
        # Lấy trạng thái mới nhất từ đỉnh stack ra
        state = stack.pop()

        # Kiểm tra nếu trạng thái hiện tại trùng với mục tiêu
        if state == goal:
            path = []
            # Truy hồi ngược từ đích về đầu dựa trên từ điển parent
            while state != start:
                path.append(state)
                state = parent[state]
            path.append(start)
            return path[::-1] # Đảo ngược để có đường đi từ đầu đến đích

        # Khám phá các trạng thái lân cận
        for next_state in get_neighbors(state):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = state # Lưu vết để tìm đường về
                stack.append(next_state)   # Thêm vào stack để tiếp tục đi sâu

    return [] # Trả về rỗng nếu không có lời giải