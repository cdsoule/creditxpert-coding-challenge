from django.shortcuts import render
from rest_framework.views import APIView
import json
import copy

class AntMoverView(APIView):
    def __init__(self):
        self.start_row = 0
        self.start_col = 0
        self.matrix = [
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0]
        ]
    
    def get(self, request):
        context = json.dumps([{"row": 0, "col": 0, "matrix": self.matrix}])
        return render(request, 'challenge2.html', {"data": context})

    def post(self, request):
        k = int(request.data['k'])

        data = json.dumps(self._ant_movement(k))

        return render(request, 'challenge2.html', {"data": data})
        
    def _ant_movement(self, k):
        matrix = self.matrix[:]
        n = len(matrix)
        m = len(matrix[0])

        # Directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        row = self.start_row
        col = self.start_col
        direction = 0

        movements = [{'row': row, 'col': col, 'matrix': copy.deepcopy(matrix)}]

        for _ in range(k):
            row += directions[direction][0]
            col += directions[direction][1]

            # wrap around
            row %= n
            col %= m

            if matrix[row][col] == 0:
                matrix[row][col] = 1
                direction = (direction + 1) % 4
            else:
                matrix[row][col] = 0
                direction = (direction - 1) % 4
            
            movements.append({'row': row, 'col': col, 'matrix': copy.deepcopy(matrix)})

        return movements

