import heapq  
def heuristic(a, b):
    """
    Tính khoảng cách Manhattan giữa 2 điểm a và b
    a, b là tuple dạng (x, y)
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def Astar_maze(maze, start, goal):
    """
    maze  : ma trận 0 (đi được) và 1 (tường)
    start : vị trí bắt đầu (x, y)
    goal  : vị trí đích (x, y)
    
    Trả về:
    parent: mảng truy vết đường đi
    """
    
    rows = len(maze)
    cols = len(maze[0])
    
    OPEN = []                              # hàng đợi ưu tiên
    heapq.heappush(OPEN, (0, start))        # đưa start vào OPEN
    
    g = {start: 0}                          # g(p): chi phí từ start → p
    parent = {start: None}                  # lưu đỉnh trước đó
    CLOSED = set()                          # tập đỉnh đã duyệt
    
    while OPEN:
        _, current = heapq.heappop(OPEN)    # lấy đỉnh có f nhỏ nhất
        
        if current in CLOSED:               # nếu đã duyệt thì bỏ qua
            continue
        
        if current == goal:                 # nếu tới goal thì dừng
            break
        
        CLOSED.add(current)
        
        x, y = current
        # duyệt 4 hướng: lên, xuống, trái, phải
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            
            # kiểm tra nằm trong biên
            if 0 <= nx < rows and 0 <= ny < cols:
                if maze[nx][ny] == 0:       # nếu không phải tường
                    
                    neighbor = (nx, ny)
                    new_g = g[current] + 1  # mỗi bước tốn 1
                    
                    # nếu chưa thấy hoặc tìm được đường tốt hơn
                    if neighbor not in g or new_g < g[neighbor]:
                        g[neighbor] = new_g
                        
                        # f = g + h
                        f = new_g + heuristic(neighbor, goal)
                        heapq.heappush(OPEN, (f, neighbor))
                        
                        parent[neighbor] = current
    
    return parent

def reconstruct_path(parent, start, goal):
    """
    Trả về danh sách đỉnh từ start → goal
    """
    if goal not in parent:
        return []
    path = []
    current = goal
    
    while current is not None:
        path.append(current)
        current = parent[current]
    
    return path[::-1]   # đảo ngược lại