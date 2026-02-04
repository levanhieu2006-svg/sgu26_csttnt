def dfs_maze(maze, start, goal):
    # Lấy số hàng và số cột của mê cung
    rows, cols = len(maze), len(maze[0])    
    # Định nghĩa các hướng di chuyển: Lên, Xuống, Trái, Phải
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    # Stack (ngăn xếp) để lưu các điểm cần khám phá (LIFO)
    stack = [start]
    # Tập hợp các điểm đã đi qua để tránh lặp vô hạn
    visited = set([start])
    # Từ điển để lưu vết: parent[điểm_hiện_tại] = điểm_trước_đó
    parent = {}
    while stack:
        # Lấy điểm cuối cùng được thêm vào stack ra để kiểm tra
        x, y = stack.pop()
        # Nếu đã đến đích
        if (x, y) == goal:
            path = []
            # Truy ngược từ đích về điểm bắt đầu dựa trên từ điển parent
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start)
            # Đảo ngược danh sách để có đường đi từ đầu đến đích
            return path[::-1]
        # Kiểm tra 4 hướng xung quanh điểm hiện tại
        for dx, dy in directions:
            nx, ny = x + dx, y + dy       
            # Điều kiện: nằm trong mê cung, là đường đi (0) và chưa từng đi qua
            if (0 <= nx < rows and 0 <= ny < cols and
                maze[nx][ny] == 0 and (nx, ny) not in visited):
                
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)
                stack.append((nx, ny))           
    # Trả về danh sách rỗng nếu không tìm thấy đường đi
    return []