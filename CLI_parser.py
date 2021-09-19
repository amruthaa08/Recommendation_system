import argparse
parser = argparse.ArgumentParser(description='select options to get recommendations')

parser.add_argument('method',
                    choices = ['cosine_similarity', 'review_based', 'user_activity_based'],
                    help = 'select method ')
parser.add_argument('cat',
                    help = 'choose product category')
parser.add_argument('-n', type = int, default = 5, metavar = 'recco_no',
                    help = 'number of recommendations required')

args = parser.parse_args()

print(args.method, args.cat, args.n)
