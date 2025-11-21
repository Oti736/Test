from collections import deque

def can_exit(maze):
    """
    Verifică dacă există o cale de ieșire dintr-un labirint (matrice 2D)
    de la (0, 0) la (R-1, C-1), deplasându-se doar pe 0 (căi libere).
    """
    R = len(maze)
    C = len(maze[0])
    
    # Punctul de plecare și cel de sosire
    start = (0, 0)
    end = (R - 1, C - 1)
    
    # Verifică dacă startul sau sosirea sunt pe un perete (1)
    if maze[start[0]][start[1]] == 1 or maze[end[0]][end[1]] == 1:
        return False
        
    # Coadă pentru BFS
    queue = deque([start])
    # Set pentru celulele vizitate
    visited = {start}
    
    # Direcțiile posibile: (rând, coloană) - Sus, Jos, Stânga, Dreapta
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        r, c = queue.popleft()
        
        # Am ajuns la ieșire
        if (r, c) == end:
            return True
        
        # Explorează vecinii
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # Verifică limitele matricei
            if 0 <= nr < R and 0 <= nc < C:
                # Dacă celula nu e perete și nu a fost vizitată
                if maze[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
                    
    # Nu s-a găsit nicio cale
    return False

# Exemple de testare din fișierul exit_maze.py:
maze1 = [
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 1, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 1, 1, 0, 0, 1],
  [1, 1, 1, 1, 1, 0, 0]
]
maze2 = [
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 0, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 0, 1, 0, 0, 1],
  [1, 1, 0, 0, 1, 1, 1]
]

print(f"Labirint 1 (True): {can_exit(maze1)}")
print(f"Labirint 2 (False): {can_exit(maze2)}")