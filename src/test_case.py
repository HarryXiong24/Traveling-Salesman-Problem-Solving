def get_test_data():
    # Test Case Result
    # Best Cost:  8
    # Best Path:  [0, 1, 2]
    # TEST_CITY_COUNT = 3
    # TEST_DISTANCE_DATA = [[0, 1, 4], [1, 0, 3], [4, 3, 0]]

    # Test Case Result
    # Best Cost:  14
    # Best Path:  [0, 1, 2, 3, 4]
    # TEST_CITY_COUNT = 5
    # TEST_DISTANCE_DATA = [
    #     [0, 1, 2, 3, 4],
    #     [1, 0, 2, 3, 4],
    #     [2, 2, 0, 3, 4],
    #     [3, 3, 4, 0, 4],
    #     [4, 3, 4, 4, 0],
    # ]

    # Test Case Result
    # Best Cost:  9
    # Best Path:  [0, 4, 2, 1, 3]
    TEST_CITY_COUNT = 5
    TEST_DISTANCE_DATA = [
        [0, 4, 3, 2, 1],
        [4, 0, 2, 3, 4],
        [3, 2, 0, 2, 1],
        [2, 3, 1, 0, 1],
        [1, 4, 1, 1, 0],
    ]

    return [
        TEST_CITY_COUNT,
        TEST_DISTANCE_DATA,
    ]
