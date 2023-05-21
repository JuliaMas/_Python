# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту,
# по которой вращается самая далекая планета.

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (11, 11)]
print(*find_farthest_orbit(orbits))

def find_farthest_orbit(orbits):
    result = 0
    res = ''
    for i in range(len(orbits)):
        if orbits[i][0] == orbits[i][1]:
            result = result
        else:
            tmp = orbits[i][0] * orbits[i][1]
            if tmp > result:
                result = tmp
                res = orbits[i]
    return res


import  math
def find_farthest_orbit(orbits):
    s_orbits = {math.pi * value[0] * value[1]: value for value in orbits if value[0] != value[1]}
    return max(s_orbits.items())[1]
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))