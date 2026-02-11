import os
from pydub import AudioSegment

def convert_mp3_to_wav(source_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output directory: {output_folder}")

    files = os.listdir(source_folder)
    mp3_files = [f for f in files if f.lower().endswith('.mp3')]
    
    if not mp3_files:
        print("No MP3 files found in the source folder.")
        return

    print(f"Found {len(mp3_files)} MP3 files. Starting conversion...\n")

    for filename in mp3_files:
        try:
            # Construct full file paths
            src_path = os.path.join(source_folder, filename)
            
            # Change extension for output
            wav_filename = os.path.splitext(filename)[0] + ".wav"
            dst_path = os.path.join(output_folder, wav_filename)

            audio = AudioSegment.from_mp3(src_path)
            audio.export(dst_path, format="wav")
            
            print(f"Converted: {filename} -> {wav_filename}")
            
        except Exception as e:
            print(f"Error converting {filename}: {e}")

    print("\n--- Conversion Complete ---")

SOURCE_DIR = 'C:/Users/admin/Downloads/.mp3' 
OUTPUT_DIR = 'C:/Users/admin/Downloads/.wav'

if __name__ == "__main__":
    if not os.path.exists(SOURCE_DIR):
        print(f"Error: Source directory '{SOURCE_DIR}' does not exist.")
        print("Please create it and put your MP3s there, or update the SOURCE_DIR variable.")
    else:
        convert_mp3_to_wav(SOURCE_DIR, OUTPUT_DIR)