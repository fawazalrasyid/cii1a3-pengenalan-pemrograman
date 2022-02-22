def read_data():
    f = open('data06.txt', 'r')

    dict_score = {}

    for row in f:
        a, score_a, score_b, b = row.split()

        dict_score[a.lower() + '_vs_' + b.lower()] = {
            a.lower() : int(score_a),
            b.lower() : int(score_b),
        }

    f.close
    return dict_score

def total_points(data):  

    # inisialisasi dict
    data_score= {}

    for k, l in data.items():

        for m, n in l.items():
            # inisialisasi goal, win, lose, draw, dan point
            goal = 0
            win = 0
            draw = 0
            lose = 0
            point = 0

            # cek apakah sebelumnya telah ada data pada key yang sama
            if data_score.get(m):
                goal += data_score[m]['goal']
                win += data_score[m]['win']
                draw += data_score[m]['draw']
                lose += data_score[m]['lose']

            # cek score maximum dan minimum dalam pertandingan
            maxi = max(l.values())
            mini = min(l.values())

            # penjumlahan
            goal += l[m]
            win += 1 if l[m] else 0
            draw += 1 if maxi == mini else 0
            lose += 1 if not l[m] else 0 
            point += (win * 2) + (draw * 1)

            # membuat dictionary baru
            data_score[m] = ({
                'goal' : goal,
                'win' : win,
                'draw' : draw,
                'lose' : lose,
                'points' : point
            })

    return data_score

def write_data(data):
    f = open('output_data06.txt', 'w')

    for k, v in data.items():
        row = k + ' ' + ' '.join(str(x) for x in v.values())
        f.write(row + '\n')

    f.close

def main():
    data_input = read_data()
    print('input : ', data_input)

    data_output = total_points(data_input)
    print('output : ', data_output)
    
    write_data(data_output)

if __name__ == '__main__':
    main()

