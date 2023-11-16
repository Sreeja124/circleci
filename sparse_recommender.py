class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = {}  # Dictionary to store non-zero values with (row, col) as keys

    def set(self, row, col, value):
        # Set the value at (row, col) to value
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[(row, col)] = value
        else:
            raise ValueError("Invalid row or column index")

    def get(self, row, col):
        # Return the value at (row, col)
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise ValueError("Invalid row or column index")
        if (row, col) in self.data:
            return self.data[(row, col)]
        else:
            return 0

    def recommend(self, vector):
        # Multiply the sparse matrix with a given vector to produce recommendations
        if len(vector) != self.cols:
            raise ValueError("Vector dimension does not match matrix columns")
        result = [0] * self.rows
        for (row, col), value in self.data.items():
            result[row] += value * vector[col]
        return result

    def add_movie(self, matrix):
        # Add another sparse matrix to this matrix
        if matrix.rows != self.rows or matrix.cols != self.cols:
            raise ValueError("Matrix dimensions do not match")
        result = SparseMatrix(self.rows, self.cols)
        for (row, col), value in self.data.items():
            result.set(row, col, value)
        for (row, col), value in matrix.data.items():
            result.set(row, col, result.get(row, col) + value)
        return result

    def to_dense(self):
        # Convert the sparse matrix to a dense matrix
        dense_matrix = [[0] * self.cols for _ in range(self.rows)]
        for (row, col), value in self.data.items():
            dense_matrix[row][col] = value
        return dense_matrix
