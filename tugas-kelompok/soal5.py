def read_data():
    f = open('data05.txt', 'r')

    dict_score = {}

    for row in f:
        name, uts, uas = row.split()
        dict_score[name] = {
            'uts' : float(uts),
            'uas' : float(uas),
        }

    f.close
    return dict_score

def average_score(data):

    for e in data:
        avg = (data[e]['uts'] + data[e]['uas']) / 2
        desc = 'pass' if avg >= 60 else  'not pass'

        data[e].update({
            'average_score' : avg,
            'desc' : desc
        })

    return data

def write_data(data):
    f = open('output_data05.txt', 'w')

    for k, v in data.items():
        row = k + ' ' + ' '.join(str(x) for x in v.values())
        f.write(row + '\n')

    f.close

def main():
    data_input = read_data()
    print('input : ', data_input)

    data_output = average_score(data_input)
    print('output : ', data_output)
    
    write_data(data_output)

if __name__ == '__main__':
    main()