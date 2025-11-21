from collections import deque

def hex_distance(grid):
    """
    Calculează distanța minimă de la primul 'x' la al doilea 'x'
    într-o grilă hexagonală folosind BFS.
    """
    R = len(grid)
    C = len(grid[0])
    start = None
    end = None
    
    # Găsește coordonatele celor două locații 'x'
    locations = []
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'x':
                locations.append((r, c))
    
    if len(locations) < 2:
        return 0 # Sau gestionează ca eroare, dar pentru exemplu presupunem 2 'x'
        
    start, end = locations[0], locations[1]
    
    # Deplasări posibile (ținând cont de aranjamentul "flat-top" sau "pointy-top", 
    # cel mai des întâlnit în reprezentările de text, care implică deplasări specifice 
    # pentru rândurile pare/impare - aici se folosesc deplasări generale pentru o grilă hexagonală)
    # Vecini posibili pentru un hexagon (dr, dc)
    # Sus-stânga, Sus-dreapta, Dreapta, Jos-dreapta, Jos-stânga, Stânga
    
    # Presupunem o grilă cu un offset la rândurile pare (odd-r horizontal layout)
    # unde vecinii depind dacă r-ul este par sau impar:
    
    # Pentru rând par (r % 2 == 0):
    directions_even = [
        (-1, 0),    # Sus-Stânga
        (-1, 1),    # Sus-Dreapta
        (0, 1),     # Dreapta
        (1, 1),     # Jos-Dreapta
        (1, 0),     # Jos-Stânga
        (0, -1)     # Stânga
    ]
    # Pentru rând impar (r % 2 != 0):
    directions_odd = [
        (-1, -1),   # Sus-Stânga
        (-1, 0),    # Sus-Dreapta
        (0, 1),     # Dreapta
        (1, 0),     # Jos-Dreapta
        (1, -1),    # Jos-Stânga
        (0, -1)     # Stânga
    ]
    
    queue = deque([(start, 0)]) # ((r, c), distanță)
    visited = {start}
    
    while queue:
        (r, c), dist = queue.popleft()
        
        if (r, c) == end:
            return dist
            
        # Alege setul de direcții în funcție de paritatea rândului
        if r % 2 == 0:
            current_directions = directions_even
        else:
            current_directions = directions_odd
            
        for dr, dc in current_directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != ' ' and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), dist + 1))
                
    return -1 # Nu s-a găsit calea

# Exemple de testare din fișierul hexagonal_grid_distance.py:
print(f"Hex Distance 1 (1): {hex_distance([ '  o o  ', ' o x o ', '  o x  ', ])}")
print(f"Hex Distance 2 (2): {hex_distance([ '  o o  ', ' x o o ', '  o x  ', ])}")
print(f"Hex Distance 3 (3): {hex_distance([ '   o o o   ', '  o o o o  ', ' o o o o o ', '  x o o x  ', '   o o o   ', ])}")