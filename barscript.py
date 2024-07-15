import pandas

def create_bars(csv, kindofbar, output):
    df = pandas.read_csv(csv)
    df.plot(kind=kindofbar).get_figure().savefig(output)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('csv')
    parser.add_argument('kindofbar')
    parser.add_argument('output')
    args = parser.parse_args()
    create_bars(args.csv, args.kindofbar, args.output)

