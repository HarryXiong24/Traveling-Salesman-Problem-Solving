def read_file(dir: str):
    # 读取用户提供的文件内容
    with open(dir, "r") as file:
        lines = file.readlines()
    CITY_COUNT = int(lines[0].strip())
    DISTANCE_DATA = [list(map(float, line.split())) for line in lines[1:]]

    return [CITY_COUNT, DISTANCE_DATA]
