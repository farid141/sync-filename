from pathlib import Path


# Initialize an empty list to store filenames
mp4_files = []
def collect_mp4():
    # Iterate through all files in the current directory
    for file_path in directory.glob("*.mp4"):
        full_filename = file_path.name
        extension_index = full_filename.find(".mp4")
        filename = full_filename[:extension_index]
        mp4_files.append(filename)
        print(filename)

def rename_subtitle():
    # Iterate through all files in the current directory
    for file_path in directory.glob("[English*"):
        # Extract the filename
        filename = file_path.name
        
        # Find the start and end index of the substring
        start_index = filename.find("[English")
        end_index = filename.find("]", start_index)
        
        # Extract the substring
        if start_index != -1 and end_index != -1:
            end_downsub = filename.find(" [DownSub.com]")
            substring = filename[end_index+2:end_downsub]
            substring = substring.replace("_", "-")

            for mp4_file in mp4_files:
                if substring in mp4_file:
                    file_path.rename(f"{mp4_file}.srt")

if __name__ == "__main__":
    # Specify the directory where your files are located
    dir=input("Insert path to the folder: ")
    directory = Path(dir)
    collect_mp4()
