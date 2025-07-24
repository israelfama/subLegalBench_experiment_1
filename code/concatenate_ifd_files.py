import json
import os
from pathlib import Path

def concatenate_json_files(input_dir, output_file):
    """
    Combine all JSON files in input_dir into a single output_file.
    
    Args:
        input_dir (str): Directory containing JSON files
        output_file (str): Path for the combined output file
    """
    combined_data = []
    
    # Get all .json files in the directory
    json_files = [f for f in Path(input_dir).glob('*.jsonl') if f.is_file()]
    
    if not json_files:
        print(f"No JSON files found in {input_dir}")
        return
    
    print(f"Found {len(json_files)} JSON files to combine")
    
    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                if isinstance(data, list):
                    combined_data.extend(data)
                else:
                    combined_data.append(data)
                    
        except Exception as e:
            print(f"Error processing {json_file}: {str(e)}")
            continue
    
    # Save the combined data
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(combined_data, f, indent=2)
    
    print(f"Successfully combined {len(combined_data)} records into {output_file}")

# Example execution when run directly
if __name__ == "__main__":
    input_directory = "/Users/israelfama/phd_thesis_projects/subLegalBench_experiment_1/data/ifd"
    output_filename = "/Users/israelfama/phd_thesis_projects/subLegalBench_experiment_1/data/concatenated_files/concatenated_ifd_gpt2.json"
    concatenate_json_files(input_directory, output_filename)