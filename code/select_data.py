import json
import numpy as np
import argparse
from tqdm import tqdm
import math
import os

concatenated_file = "concatenated_ifd_gpt2.json"
concatenated_directory = "/Users/israelfama/phd_thesis_projects/subLegalBench_experiment_1/data/concatenated_files"
concatenated_data_path = os.path.join(concatenated_directory,concatenated_file)
sample_file = "selected_data_gpt2.json"
sample_directory = "/Users/israelfama/phd_thesis_projects/subLegalBench_experiment_1/data/selected_data"
selected_data_path = os.path.join(sample_directory,sample_file)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--concatenated_data_path", type=str, default=concatenated_data_path)
    parser.add_argument("--selected_data_path", type=str, default=selected_data_path)
    parser.add_argument("--sample_rate", type=float, default=0.01)
    parser.add_argument("--filter_threash", type=float, default=1)
    parser.add_argument("--key_name", type=str, default="ifd_ppl", help="ifd_ppl")
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    print(args)

    with open(args.concatenated_data_path, "r") as f:
        json_data = json.load(f)
    
    sample_num = int(len(json_data)*args.sample_rate)

    def sort_key(x):
        if math.isnan(x[args.key_name]):
            return(0,0)
        return (1, x[args.key_name])
    
    filtered_data = [x for x in json_data if (isinstance(x[args.key_name], (int, float)) and x[args.key_name] < args.filter_threash)]
    new_data = sorted(filtered_data, key=sort_key, reverse=True)

    new_data = new_data[:sample_num]
    print(len(new_data))

    with open(args.selected_data_path, "w") as file:
        json.dump(new_data, file, indent=4)
    
    print("Done: Data Selection:", args.selected_data_path)



if __name__ == "__main__":
    main()

