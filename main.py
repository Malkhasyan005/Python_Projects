def get_info_about_cities(filename):
    with open(filename) as f:
        return f.read()

def get_cities_dict(fcnt):
    md = {}
    f = fcnt.replace('\n\t', " ")
    ml = f.split('\n')
    for el in ml[:-1]:
        names = el.split(':')
        md[names[0]] = names[1]

    return md

def get_way_size(cities):
    md = {}
    for el in cities:
        name_way = el.split('/')
        md[name_way[0]] = name_way[1]

    return md

def get_city_name(way_size, where):
    for el in way_size:
        if el.find(where) == 0:
            return el


def get_way_passed(way_size, name):
    way = 0
    for el in way_size:
        if el != name:
            way += int(way_size[el])
        else:
            break
    return way
    

def get_all_way(way_size):
    all_way = 0
    for el in way_size:
        all_way += int(way_size[el])
    return all_way

def creat_new_cities_in_way(city_count):
    ml = []
    for i in range(city_count):
        city = input("Enter the citi name on the road and way(city-city/way): ")
        ml.append(city)
            
    return ml

def add_new_way_in_file(filename, direct, names):
    with open(filename, "a") as f:
        f.write(direct + ":\n")
        for el in names:
            f.write("\t" + el + "\n")

def if_is_direction_name(city_name_dict, from_where):
    way_cities = city_name_dict[from_where].split()
    way_size = get_way_size(way_cities)
    where = input('Enter your location:  ')
    city = get_city_name(way_size, where)
    all_way = get_all_way(way_size)
    way_passed = get_way_passed(way_size, city)
    way_stay = all_way - way_passed
    print(f"You passed {way_passed}km, there are {way_stay}km left")

def if_not_direction_name(filename):
    direction = input("There is no such direction.Please enter the given direction(city-city):  ")
    count_cities = int(input("Enter the number of cities on the road:  "))
    names_cities = creat_new_cities_in_way(count_cities)
    add_new_way_in_file(filename, direction, names_cities)

def main():
    filename = 'routes.txt'
    content = get_info_about_cities(filename)
    city_name_dict = get_cities_dict(content)
    from_where = input("Enter direction:   ")
    if from_where in city_name_dict:
        if_is_direction_name(city_name_dict, from_where)
    else:
        if_not_direction_name(filename)


if __name__ == '__main__':
    main()
