# 定义剪枝函数
# 这么定界的原因是: 任何有效的解决方案都必须包括从每个城市出发到另一个城市的边，因此，对于每个城市，至少有一个进入和一个离开的边
# 通过计算每个城市的最小和第二小边的值，然后将这些值累加起来除以2，是一个合理估计
# 下面两个函数就是获取最小和第二小边值的函数
# 获取最小边
from typing import List


def first_min(distance_data: List[List[float]], city_count: int, current_city: int):
    min_val = float("inf")
    for i in range(city_count):
        if distance_data[current_city][i] < min_val and current_city != i:
            min_val = distance_data[current_city][i]
    return min_val


# 获取第二小边
def second_min(distance_data: List[List[float]], city_count: int, current_city: int):
    first, second = float("inf"), float("inf")
    for i in range(city_count):
        if current_city == i:
            continue
        if distance_data[current_city][i] <= first:
            second = first
            first = distance_data[current_city][i]
        elif first < distance_data[current_city][i] <= second:
            second = distance_data[current_city][i]
    return second


def branch_and_bound(
    city_count: int, distance_data: List[List[float]]
) -> [float, List[int]]:
    # 定义无穷大作为初始的最小路径长度
    best_path_cost = float("inf")
    best_path = []
    # 创建一个路径列表来保存当前路径
    path = [-1] * city_count

    # DFS 来实现分支定界
    # bound：当前搜索分支的下界估计值
    # weight：当前路径的总权重（距离）
    # level：搜索树的深度，即路径中已经访问的城市数量
    # path：当前路径，是一个包含访问过的城市序号的列表
    def recursive(bound: int, weight: int, level: int, path: List[int]):
        nonlocal best_path_cost, best_path
        # 如果我们到达了最后一层
        if level == city_count:
            # 检查是否可以形成回路，如果值不为 0，说明存在一条从最后一个城市回到起始城市的路径，可以形成闭环
            if distance_data[path[level - 1]][path[0]] != 0:
                # 计算总成本
                curr_res = weight + distance_data[path[level - 1]][path[0]]
                if curr_res < best_path_cost:
                    best_path_cost = curr_res
                    best_path = path.copy()
            return

        # 遍历所有顶点来构建递归树
        for i in range(city_count):
            # 检查是否可以访问该顶点
            if distance_data[path[level - 1]][i] != 0 and i not in path:
                temp = bound
                weight += distance_data[path[level - 1]][i]

                # 计算 bound
                if level == 1:
                    bound -= (
                        first_min(distance_data, city_count, path[level - 1])
                        + first_min(distance_data, city_count, i)
                    ) / 2
                else:
                    bound -= (
                        second_min(distance_data, city_count, path[level - 1])
                        + first_min(distance_data, city_count, i)
                    ) / 2

                # bound + weight 是当前解的下界
                if bound + weight < best_path_cost:
                    path[level] = i
                    recursive(bound, weight, level + 1, path.copy())

                # 恢复前一个 bound 和 weight
                weight -= distance_data[path[level - 1]][i]
                bound = temp

                # 清除路径
                path[level] = -1

    # 第一个顶点总是第一个被访问的
    path[0] = 0

    # 通过计算每个城市的最小和第二小边的值，然后将这些值累加起来除以2，这为一个合理的 bound 估计方法
    bound = (
        sum(first_min(distance_data, city_count, i) for i in range(city_count))
        + sum(second_min(distance_data, city_count, i) for i in range(city_count))
    ) / 2

    # 调用递归函数
    recursive(bound, 0, 1, path)
    return [best_path_cost, best_path]
