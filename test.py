import pytest
from sparse_recommender import SparseMatrix

# Initialize a SparseMatrix for testing
def setup_test_matrix():
    matrix = SparseMatrix(3, 3)
    matrix.set(0, 0, 1)
    matrix.set(0, 1, 2)
    matrix.set(1, 1, 3)
    matrix.set(2, 2, 4)
    return matrix

# Test cases for the SparseMatrix class
def test_set_and_get():
    matrix = setup_test_matrix()
    assert matrix.get(0, 0) == 1
    assert matrix.get(0, 1) == 2
    assert matrix.get(1, 1) == 3
    assert matrix.get(2, 2) == 4

def recommend(self, vector):
    # Multiply the sparse matrix with a given vector to produce recommendations
    if len(vector) != self.cols:
        raise ValueError("Vector dimension does not match matrix columns")
    result = [0] * self.rows
    for (row, col), value in self.data.items():
        print(f"Multiplying ({row}, {col}): {value} * {vector[col]}")
        result[row] += value * vector[col]
    return result

def test_add_movie():
    matrix1 = setup_test_matrix()
    matrix2 = SparseMatrix(3, 3)
    matrix2.set(1, 0, 5)
    matrix2.set(2, 1, 6)
    result = matrix1.add_movie(matrix2)
    assert result.get(1, 0) == 5
    assert result.get(2, 1) == 6

def test_to_dense():
    matrix = setup_test_matrix()
    dense_matrix = matrix.to_dense()
    assert dense_matrix == [[1, 2, 0], [0, 3, 0], [0, 0, 4]]

def test_invalid_set():
    matrix = setup_test_matrix()
    # Try to set a value at an invalid row or column index
    with pytest.raises(ValueError):
        matrix.set(4, 2, 5)

def test_invalid_get():
    matrix = setup_test_matrix()
    # Try to get a value at an invalid row or column index
    try:
        matrix.get(3, 1)
        # If no exception is raised, fail the test
        assert False, "Expected ValueError but no exception was raised"
    except ValueError as e:
        # Check if the exception is of type ValueError
        assert str(e) == "Invalid row or column index"


def test_invalid_vector_dimensions():
    matrix = setup_test_matrix()
    vector = [1, 2]  # Vector with incorrect dimensions
    # Try to recommend with a vector of incorrect dimensions
    with pytest.raises(ValueError):
        matrix.recommend(vector)

def test_invalid_matrix_addition():
    matrix1 = setup_test_matrix()
    matrix2 = SparseMatrix(2, 2)  # Matrix with different dimensions
    # Try to add matrices with different dimensions
    with pytest.raises(ValueError):
        matrix1.add_movie(matrix2)

def test_to_dense():
    matrix = setup_test_matrix()
    dense_matrix = matrix.to_dense()
    # Check if the dense matrix has the correct dimensions
    assert len(dense_matrix) == 3
    assert len(dense_matrix[0]) == 3
    assert len(dense_matrix[1]) == 3
    assert len(dense_matrix[2]) == 3
    # Check if the dense matrix values match the sparse matrix
    assert dense_matrix == [[1, 2, 0], [0, 3, 0], [0, 0, 4]]

def test_add_movie_with_overlap():
    matrix1 = setup_test_matrix()
    matrix2 = SparseMatrix(3, 3)
    matrix2.set(1, 1, 5)  # Add a value that overlaps with matrix1
    result = matrix1.add_movie(matrix2)
    # Check if the result contains the combined values correctly
    assert result.get(0, 0) == 1
    assert result.get(0, 1) == 2
    assert result.get(1, 1) == 8  # Combined value
    assert result.get(2, 2) == 4

def test_add_movie_no_overlap():
    matrix1 = setup_test_matrix()
    matrix2 = SparseMatrix(3, 3)
    matrix2.set(1, 0, 5)  # Add a value that does not overlap with matrix1
    result = matrix1.add_movie(matrix2)
    # Check if the result contains the combined values correctly
    assert result.get(0, 0) == 1
    assert result.get(0, 1) == 2
    assert result.get(1, 0) == 5  # Added value
    assert result.get(1, 1) == 3
    assert result.get(2, 2) == 4
    
if __name__ == "__main__":
    pytest.main()
