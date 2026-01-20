def minimize_distance(points):
    """
    Calculates the minimum total distance to a point B (the median).
    """
    points.sort()  # Sorting is essential to find the median
    n = len(points)
    median_index = n // 2
    B = points[median_index]
    
    total_distance = sum(abs(x - B) for x in points)
    return total_distance

if __name__ == "__main__":
    # Test cases
    data = [1, 5, 2, 7, 10]
    result = minimize_distance(data)
    print(f"The minimum total distance for {data} is: {result}")
