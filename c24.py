from itertools import combinations

def output_list_to_file(output_file, cclist):
    with  open(output_file, "w") as text_file:
        cnt = 0
        for cc in cclist:
            text_file.write(str(cc)+'\n')
            cnt = cnt + 1
    print("output to file {0}, total {1} items".format(output_file, cnt))
    return

def output_list(result_list):
    for ii in result_list:
        print(ii)

def perfrom_stupid_filter(cclist):
    # it takes lots of memory
    allmiss = []
    onehit = []
    twohit = []
    answer = set( range(1,13) )
    cnt = 0
    for cc in cclist:
        cnt += 1
        try:
            union_set = set(cc) & answer
            if len( union_set ) == 0:
                allmiss.append(cc)
            elif len( union_set ) == 1:
                onehit.append(cc)
            elif len( union_set ) == 2:
                twohit.append(cc)
        except:
            print('shit happens')
            continue
    print('>>> all combinations: {}'.format(cnt))
    print('>>> allmiss')
    output_list(allmiss)
    print('>>> onehit, size: {}'.format(len(onehit)))
    output_list(onehit)
    print('>>> twohit, size: {}'.format(len(twohit)))
    output_list(twohit)
    return



def main():
    output_file = 'out.txt'
    # a = [1,2,3,...,22,23,24]
    a = range(1,25)
    # ii = C(24, 12)
    ii = combinations(a, 12)
    #output_list_to_file(output_file, ii)
    perfrom_stupid_filter(ii)
    return

if __name__ == '__main__':
    main()
