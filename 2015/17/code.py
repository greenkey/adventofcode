
def get_list_using_mask(obj_list,mask):
    s = list()
    mask = "{0:b}".format(mask)
    for i in range(len(mask)):
        if mask[-i-1] == '1':
            s.insert(0,obj_list[-i-1])
    return s

def sum_using_mask(numbers,mask):
    return sum(get_list_using_mask(numbers,mask))

def container_combination(volume,containers):
    count = 0
    print(containers)
    for i in range(pow(2,len(containers))):
        if volume == sum_using_mask(containers,i):
            count += 1
    return count


if __name__ == "__main__":
    with open('input', 'r') as container_list:
        containers = map( lambda x: int(x), container_list.read().split("\n") )

    eggnog_liters = 150
    print("Combination of containers: {}".format( container_combination( volume=eggnog_liters, containers=containers ) ))