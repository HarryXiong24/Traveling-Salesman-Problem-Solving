from src.sls import sls
from src.bnb_bt_dfs import branch_and_bound
from src.generate_travelling_salesman_problem import write_distance_matrix
from src.read_input import read_file
from src.test_case import get_test_data

if __name__ == "__main__":
    # Generate the data
    n = int(input("Enter the number of locations: "))
    mean = float(input("Enter the mean: "))
    sigma = float(input("Enter the standard deviation: "))
    file_name = write_distance_matrix(n, mean, sigma)

    # Read File
    [CITY_COUNT, DISTANCE_DATA] = read_file(file_name)

    # Test Case
    # CITY_COUNT, DISTANCE_DATA = get_test_data()

    # Apply the Branch and Bound algorithm to find the shortest path for the TSP
    best_cost, best_path = branch_and_bound(CITY_COUNT, DISTANCE_DATA)
    current_cost, current_path = sls(CITY_COUNT, DISTANCE_DATA, 100)

    # Print Result
    print("BnB Result")
    print("Best Cost: ", best_cost)
    print("Best Path: ", best_path)
    print("SLS Result")
    print("Best Cost: ", best_cost)
    print("Best Path: ", best_path)
