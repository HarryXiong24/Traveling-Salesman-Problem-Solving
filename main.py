from src.sls_single_process import sls_single_process
from src.sls_multi_precesses import sls_multi_precesses
from src.bnb_bt_dfs import branch_and_bound
from src.generate_travelling_salesman_problem import write_distance_matrix
from src.read_input import read_file
from src.test_case import get_test_data
import time

if __name__ == "__main__":
    # Generate the data
    # n = int(input("Enter the number of locations: "))
    # mean = float(input("Enter the mean: "))
    # sigma = float(input("Enter the standard deviation: "))
    # file_name = write_distance_matrix(n, mean, sigma)

    # Read File
    # [CITY_COUNT, DISTANCE_DATA] = read_file(file_name)

    # Test Case
    CITY_COUNT, DISTANCE_DATA = get_test_data()

    # Test BnB
    bnb_start_time = time.time()
    # Apply the Branch and Bound algorithm to find the shortest path for the TSP
    bnb_best_cost, bnb_best_path = branch_and_bound(CITY_COUNT, DISTANCE_DATA)
    bnb_end_time = time.time()

    # Print Result
    print("BnB Result")
    print("Best Cost: ", bnb_best_cost)
    print("Best Path: ", bnb_best_path)
    print(f"Time Consume: {bnb_end_time-bnb_start_time} seconds")

    # Test SLS
    sls_start_time = time.time()
    sls_best_cost, sls_best_path = sls_single_process(CITY_COUNT, DISTANCE_DATA, 100)
    sls_end_time = time.time()

    # Print Result
    print("SLS Result(single-process)")
    print("Best Cost: ", sls_best_cost)
    print("Best Path: ", sls_best_path)
    print(f"Time Consume: {sls_end_time-sls_start_time} seconds")

    # Test SLS
    sls_start_time = time.time()
    sls_best_cost, sls_best_path = sls_multi_precesses(
        CITY_COUNT, DISTANCE_DATA, 100, 1
    )
    sls_end_time = time.time()

    # Print Result
    print("SLS Result(multi-processes)")
    print("Best Cost: ", sls_best_cost)
    print("Best Path: ", sls_best_path)
    print(f"Time Consume: {sls_end_time-sls_start_time} seconds")
