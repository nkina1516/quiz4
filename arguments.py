#Argparse module to parse input arguments
import argparse

def demo() -> None:
    parser= argparse.ArgumentParser()
    parser.add_argument(help="Enter a path",dest="input_path",type=str)
    parser.add_argument(help="Enter a number",dest="number",type=int)
    parser.add_argument(help="Enter a number",dest="double",type=float)
    args=parser.parse_args()

    path=args.input_path
    num=args.number
    num2=args.double

    print("The path is: ",path)
    print("the number is : ",num)
    print("The double is: ", num2)

if __name__=='__main__': 	
    demo()


