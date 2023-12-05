import random
from typing import List
from multiprocessing import Pool


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
    current_path: List[int], distance_data: List[List[float]], segment: range
) -> tuple[List[int], float]:
    min_distance = calculate_total_distance(current_path, distance_data)
    best_path = current_path
    for i in segment:
        for j in range(i + 1, len(current_path)):
            new_path = current_path.copy()
            new_path[i], new_path[j] = new_path[j], new_path[i]
            new_distance = calculate_total_distance(new_path, distance_data)
            if new_distance < min_distance:
                min_distance = new_distance
                best_path = new_path
    return (best_path, min_distance)


def find_best_parallel(
    current_path: List[int], distance_data: List[List[float]], processes_count: int
) -> tuple[List[int], float]:
    # 将路径分割为多个段，每个进程处理一个段
    segments = [
        range(i, len(current_path), processes_count) for i in range(processes_count)
    ]

    with Pool(processes=processes_count) as pool:
        results = pool.starmap(
            find_best,
            [(current_path, distance_data, segment) for segment in segments],
        )

    # 找到所有子集中的最佳路径
    min_distance = float("inf")
    best_path = None
    for path, distance in results:
        if distance < min_distance:
            min_distance = distance
            best_path = path

    return (best_path, min_distance)


def sls_multi_precesses(
    city_count: int,
    distance_data: List[List[float]],
    exec_count_limit: int,
    processes_count: int = 1,
) -> tuple[float, List[int]]:
    # 初始化路径为城市的顺序排列
    current_path = list(range(city_count))
    random.shuffle(current_path)  # 随机打乱路径
    current_distance = calculate_total_distance(current_path, distance_data)

    for _ in range(exec_count_limit):
        new_path, new_distance = find_best_parallel(
            current_path.copy(), distance_data, processes_count
        )

        # 如果新路径的距离更短，则接受这个新路径
        if new_distance < current_distance:
            current_path = new_path
            current_distance = new_distance

    return (current_distance, current_path)
