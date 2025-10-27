import pandas as pd
import os
import glob

def formatting_csv(csv_file):
    df = pd.read_csv(csv_file, header=None)
    df.rename(columns={0: 'start_time', 1: 'end_time', 2: 'annotation'}, inplace=True)

    audio_extensions = ['wav', 'm4a', 'mp3']
    audio_folder = '/home/dhind/Kauai-Amakihi/Kauai Amakihi - Macaulay Recordings'
    base_name = os.path.splitext(os.path.basename(csv_file))[0]

    matched_file = None
    for ext in audio_extensions:
        pattern = os.path.join(audio_folder, '**', f'*{base_name}*.{ext}')
        matches = glob.glob(pattern, recursive=True)
        print(f"Searching for: {pattern}")
        print(f"Found matches: {matches}")

        for m in matches:
            audio_base = os.path.splitext(os.path.basename(m))[0].lower()
            if base_name.lower() in audio_base:
                matched_file = m
                break

        if matched_file:
            break

    if matched_file:
        relative_path = os.path.abspath(matched_file)
    else:
        print(f"No match found for {base_name}")
        relative_path = f"{audio_folder}/{base_name}.UNKNOWN"

    df['file'] = relative_path

    output_path = os.path.join(
        "Kauai-Amakihi/Annotations/macaulay/csv files/reformatted files",
        f"{base_name}reform.csv"
    )
    df.to_csv(output_path, index=False)
    print(f"Matched file: {matched_file if matched_file else 'None found'}")

# Filter only CSV files
path = "Kauai-Amakihi/Annotations/macaulay/csv files/"
dir_list = [f for f in os.listdir(path) if f.endswith('.csv')]

for item in dir_list:
    full_path = os.path.join(path, item)
    formatting_csv(full_path)
    print(f"Conversion complete: {item} reformatted using pandas")
