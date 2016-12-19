

def dragon_generate(data):
    return data + '0' + ''.join(['1' if c=='0' else '0' for c in data[::-1]])

def checksum(data):
    while len(data)%2==0:
        data = ''.join(['1' if c[0]==c[1] else '0' for c in [data[i*2:i*2+2] for i in range(int(len(data)/2))]])
    return data



if __name__ == '__main__':
    import sys

    disk_length = int(sys.argv[1])
    data = sys.argv[2]

    while len(data) < disk_length:
        data = dragon_generate(data)

    data = data[:disk_length]

    print(checksum(data))
    # this is enough for both the steps
