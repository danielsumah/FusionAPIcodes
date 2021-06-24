def main():
    number_of_points = eval(input('Enter Number of Points: '))
    distance_between_points = eval(input('Enter Distance between each points: '))

    number_of_points_on_one_side_of_origin = number_of_points // 2

    point_list = []

    if number_of_points % 2 == 0:
        point_right = distance_between_points / 2
        
        for point in range(number_of_points_on_one_side_of_origin):
            point_list.append(point_right)
            point_right +=distance_between_points

        point_left = -(distance_between_points / 2)
        for point in range(number_of_points_on_one_side_of_origin):
            point_list.append(point_left)
            point_left -=distance_between_points

        point_list.sort()
        print(point_list)

    else:
        origin = 0
        point_list.append(origin)

        point_right = distance_between_points
        for point in range(number_of_points_on_one_side_of_origin):
            point_list.append(point_right)
            point_right +=distance_between_points

        point_left = -distance_between_points
        for point in range(number_of_points_on_one_side_of_origin):
            point_list.append(point_left)
            point_left -=distance_between_points

        point_list.sort()

        # print out the list of coordinates
        # print(point_list)

    point_bucket = []
    
    for i in point_list:
        point_bucket.append([i,0,0])
    print(point_bucket)
main()