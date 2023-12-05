from src.sls_single_start import sls_single_start
from src.sls_multi_start import sls_multi_start
from src.bnb_bt_dfs import branch_and_bound
from src.util import get_cpu_count
from src.generate_travelling_salesman_problem import write_distance_matrix
from src.read_input import read_file
from src.test_case import get_test_data
import time

# from test.sls_multi_precesses import sls_multi_precesses

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
    exec_count_limit = 1000000

    print("\n")

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
    print("\n")

    # Test SLS
    sls_start_time_1 = time.time()
    sls_best_cost_1, sls_best_path_1 = sls_single_start(
        CITY_COUNT, DISTANCE_DATA, exec_count_limit
    )
    sls_end_time_1 = time.time()

    # Print Result
    print("SLS Result(single-start)")
    print("Best Cost: ", sls_best_cost_1)
    print("Best Path: ", sls_best_path_1)
    print(f"Time Consume: {sls_end_time_1-sls_start_time_1} seconds")
    print("\n")

    # Test SLS
    cpu_count = get_cpu_count()
    sls_start_time_2 = time.time()
    sls_best_cost_2, sls_best_path_2 = sls_multi_start(
        CITY_COUNT, DISTANCE_DATA, exec_count_limit, cpu_count
    )
    sls_end_time_2 = time.time()

    # Print Result
    print("SLS Result(multi-start)")
    print("Best Cost: ", sls_best_cost_2)
    print("Best Path: ", sls_best_path_2)
    print(f"Time Consume: {sls_end_time_2-sls_start_time_2} seconds")
    print("\n")

    # Test SLS
    # sls_start_time_3 = time.time()
    # sls_best_cost_3, sls_best_path_3 = sls_multi_precesses(
    #     CITY_COUNT, DISTANCE_DATA, 1000000, 4
    # )
    # sls_end_time_3 = time.time()

    # # Print Result
    # print("SLS Result(multi-processes)")
    # print("Best Cost: ", sls_best_cost_3)
    # print("Best Path: ", sls_best_path_3)
    # print(f"Time Consume: {sls_end_time_3-sls_start_time_3} seconds")
    # print("\n")
