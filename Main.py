import argparse

import collectData
import dispPassages
import outputData
#disp = display passages
#out = output to txt
#col = collect and display

# Add arguments
parser = argparse.ArgumentParser(description='captures sentences and performs operations')
parser.add_argument('arg1', help='operation')
parser.add_argument('arg2', help='expression')
parser.add_argument('arg3', type=int, help='pgs')
# Parse the command-line arguments
args = parser.parse_args()
if args.arg1 == "disp":
    dispPassages.dispP()
elif args.arg1 == "collect":
    collectData.data(args.arg2, args.arg3)
elif args.arg1 == "output":
    outputData.output(args.arg2, args.arg3)
