from multiprocessing import Pool
import os
import random
from typing import List


def calculate_total_distance(
    path: List[int], distance_data: List[List[float]]
) -> float:
    total_distance = 0.0
    # 遍历路径中的每一对连续城市
    for i in range(len(path)):
        # 累加从当前城市到下一个城市的距离
        # 比如有 4 个城市的路径，当 i = 3 时，path[(i + 1) % len(path)] 将会是 path[0]
        # 可以计算从最后一个城市回到第一个城市的距离
        total_distance += distance_data[path[i]][path[(i + 1) % len(path)]]
    return total_distance


def find_best(
    current_path: List[int], distance_data: List[List[float]]
) -> tuple[List[int], float]:
    min_distance = calculate_total_distance(current_path, distance_data)
    best_path = current_path
    for i in range(0, len(current_path)):
        for j in range(i + 1, len(current_path)):
            new_path = current_path.copy()
            new_path[i], new_path[j] = new_path[j], new_path[i]
            new_distance = calculate_total_distance(new_path, distance_data)
            if new_distance < min_distance:
                min_distance = new_distance
                best_path = new_path
    return (best_path, min_distance)


def find_best_from_random_start(
    city_count: int, distance_data: List[List[float]]
) -> tuple[List[int], float]:
    # 初始化路径为城市的顺序排列
    current_path = list(range(city_count))
    # 随机打乱路径
    random.shuffle(current_path)
    return find_best(current_path, distance_data)


def sls_multi_processes(
    city_count: int,
    distance_data: List[List[float]],
    exec_count_limit: int,
    processes_count: int = 1,
) -> tuple[float, List[int]]:
    best_global_distance = float("inf")
    best_global_path = None

    with Pool(processes=processes_count) as pool:
        results = pool.starmap(
            find_best_from_random_start,
            [(city_count, distance_data) for _ in range(exec_count_limit)],
        )

    for path, distance in results:
        if distance < best_global_distance:
            best_global_distance = distance
            best_global_path = path

    return (best_global_distance, best_global_path)
