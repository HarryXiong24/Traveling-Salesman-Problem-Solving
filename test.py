import csv
import os
import time
from src.sls_multi_processes import sls_multi_processes
from src.bnb_dfs_single_process import branch_and_bound_single_process
import concurrent.futures


def read_tsp_file(file_path):
    with open(file_path, "r") as file:
        n = int(file.readline().strip())
        matrix = [list(map(float, line.split())) for line in file]
    return n, matrix


def run_algorithm_with_timeout(city_count, distance_matrix):
    timeout_seconds = 600  # 10 minutes
    start_time = time.time()

    with concurrent.futures.ProcessPoolExecutor(max_workers=1) as executor:
        future = executor.submit(
            branch_and_bound_single_process,
            city_count,
            distance_matrix,
        )
        try:
            best_distance, best_solution = future.result(timeout=timeout_seconds)
        except concurrent.futures.TimeoutError:
            return None, None, timeout_seconds

    end_time = time.time()
    return best_solution, best_distance, end_time - start_time


def process_tsp_files(folder_path, output_csv, group_number, student_ids):
    files = os.listdir(folder_path)
    files.sort(key=lambda x: int(x.split("-")[2]))

    with open(output_csv, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([group_number])
        writer.writerow([student_ids])
        writer.writerow(["SLS"])

        timeout_occurred = False
        for filename in files:
            if filename.endswith(".txt"):
                writer.writerow([filename])
                if not timeout_occurred:
                    n, distance_matrix = read_tsp_file(
                        os.path.join(folder_path, filename)
                    )
                    solution, distance, time_taken = run_algorithm_with_timeout(
                        n, distance_matrix
                    )
                    if solution is None:  # Timeout occurred
                        timeout_occurred = True
                        writer.writerow(["Solution Path", "No Path Found"])
                        writer.writerow(["Tour Length", "No Solution"])
                        writer.writerow(["CPU Runtime", "N/A"])
                    else:
                        writer.writerow(
                            ["Solution Path", "->".join(map(str, solution))]
                        )
                        writer.writerow(["Tour Length", distance])
                        writer.writerow(["CPU Runtime", time_taken])
                else:
                    # Record empty values for the unprocessed files due to timeout
                    writer.writerow(["Solution Path", ""])
                    writer.writerow(["Tour Length", ""])
                    writer.writerow(["CPU Runtime", ""])


if __name__ == "__main__":
    group_number = "66"  # Group number
    student_ids = "90567289, 42249152, 87606914"  # Student IDs
    tsp_folder_path = "./competition/"  # Path to your TSP files
    results_csv_path = "./results_bnb.csv"  # Path for the results CSV
    process_tsp_files(tsp_folder_path, results_csv_path, group_number, student_ids)
