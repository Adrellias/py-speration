import multiprocessing as mp

def f(x):
    f.q.put('Doing: ' + str(x))
    return x*x

def f_init(q):
    f.q = q

def main():
    #jobs = range(1,16)

    jobs = [ 1,20,3,8,15,12,10,4,2,5,8,22,23,30,5,8,2,1 ]
    q = mp.Queue()
    p = mp.Pool(None, f_init, [q])
    results = p.imap(f, jobs)
    p.close()

    for i in jobs:
        print i
        print q.get()
        print results.next()

if __name__ == '__main__':
    main()
