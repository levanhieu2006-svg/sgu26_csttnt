import heapq
def get_neighbors(state):
    """
    state: tuple 9 phần tử
    Trả về danh sách trạng thái kề
    """
    neighbors = []
    
    idx = state.index(0)           # vị trí ô trống
    row, col = divmod(idx, 3)
    
    # 4 hướng di chuyển
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    
    for dx, dy in moves:
        nr, nc = row + dx, col + dy
        
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_idx = nr*3 + nc
            
            # hoán đổi 0 với ô bên cạnh
            new_state = list(state)
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            
            neighbors.append(tuple(new_state))
    
    return neighbors

def heuristic_puzzle(state, goal):
    """
    Tổng khoảng cách Manhattan của từng ô (1→8)
    """
    distance = 0
    
    for num in range(1, 9):
        i = state.index(num)
        gi = goal.index(num)
        
        x1, y1 = divmod(i, 3)
        x2, y2 = divmod(gi, 3)
        
        distance += abs(x1 - x2) + abs(y1 - y2)
    
    return distance

def Astar_puzzle(start, goal):
    """
    start, goal: tuple 9 phần tử
    """
    
    OPEN = []
    heapq.heappush(OPEN, (0, start))
    
    g = {start: 0}                 # chi phí thật
    parent = {start: None}         # truy vết
    CLOSED = set()
    
    while OPEN:
        _, current = heapq.heappop(OPEN)
        
        if current in CLOSED:
            continue
        
        if current == goal:
            break
        
        CLOSED.add(current)
        
        # duyệt các trạng thái kề
        for neighbor in get_neighbors(current):
            
            new_g = g[current] + 1   # mỗi bước tốn 1
            
            # nếu tìm được đường tốt hơn
            if neighbor not in g or new_g < g[neighbor]:
                g[neighbor] = new_g
                
                f = new_g + heuristic_puzzle(neighbor, goal)
                heapq.heappush(OPEN, (f, neighbor))
                
                parent[neighbor] = current
    
    return parent