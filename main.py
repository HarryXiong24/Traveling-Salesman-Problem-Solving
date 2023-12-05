from src.sls_single_process import sls_single_process
from src.sls_multi_processes import sls_multi_processes
from src.bnb_dfs_single_process import branch_and_bound_single_process
from src.util import get_cpu_count
from src.generate_travelling_salesman_problem import write_distance_matrix
from src.read_input import read_file
from src.test_case import get_test_data
import time

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

    exec_count_limit = 100000
    cpu_count = get_cpu_count()

    print("--------------------")

    # Test BnB
    bnb_start_time_1 = time.time()
    # Apply the Branch and Bound algorithm to find the shortest path for the TSP
    bnb_best_cost_1, bnb_best_path_1 = branch_and_bound_single_process(
        CITY_COUNT, DISTANCE_DATA
    )
    bnb_end_time_1 = time.time()

    # Print Result
    print("BnB Result(single-process)")
    print("Best Cost: ", bnb_best_cost_1)
    print("Best Path: ", bnb_best_path_1)
    print(f"Time Consume: {bnb_end_time_1-bnb_start_time_1} seconds")
    print("--------------------")

    # Test SLS
    sls_start_time_1 = time.time()
    sls_best_cost_1, sls_best_path_1 = sls_single_process(
        CITY_COUNT, DISTANCE_DATA, exec_count_limit
    )
    sls_end_time_1 = time.time()

    # Print Result
    print("SLS Result(single-process)")
    print("Limit: ", exec_count_limit)
    print("Best Cost: ", sls_best_cost_1)
    print("Best Path: ", sls_best_path_1)
    print(f"Time Consume: {sls_end_time_1-sls_start_time_1} seconds")
    print("--------------------")

    # Test SLS
    sls_start_time_2 = time.time()
    sls_best_cost_2, sls_best_path_2 = sls_multi_processes(
        CITY_COUNT, DISTANCE_DATA, exec_count_limit, cpu_count
    )
    sls_end_time_2 = time.time()

    # Print Result
    print("SLS Result(multi-processes)")
    print("Limit: ", exec_count_limit)
    print("Best Cost: ", sls_best_cost_2)
    print("Best Path: ", sls_best_path_2)
    print(f"Time Consume: {sls_end_time_2-sls_start_time_2} seconds")
    print("--------------------")
