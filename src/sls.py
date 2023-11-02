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


def sls(
    city_count: int, distance_data: List[List[float]], time_limit: int
) -> [float, List[int]]:
    # 初始化路径为城市的顺序排列
    current_path = list(range(city_count))
    random.shuffle(current_path)  # 随机打乱路径
    current_distance = calculate_total_distance(current_path, distance_data)

    for _ in range(time_limit):
        # 随机选择两个不同的城市
        city1, city2 = random.sample(range(city_count), 2)
        # 交换两个城市的位置
        new_path = current_path.copy()
        new_path[city1], new_path[city2] = new_path[city2], new_path[city1]
        # 计算新路径的总距离
        new_distance = calculate_total_distance(new_path, distance_data)

        # 如果新路径的距离更短，则接受这个新路径
        if new_distance < current_distance:
            current_path = new_path
            current_distance = new_distance

    return [current_distance, current_path]
