import os
from mutagen.easyid3 import EasyID3

def update_filenames(directory):
    renamed_files = []  # Array to store renamed filenames

    for filename in os.listdir(directory):
        if filename.endswith(".mp3"):
            filepath = os.path.join(directory, filename)

            try:
                # Load audio file metadata
                audiofile = EasyID3(filepath)

                # Get the title from the metadata
                if 'title' in audiofile:
                    title = audiofile['title'][0]
                    new_filename = f"{title}.mp3"
                    
                    # Rename the file
                    os.rename(filepath, os.path.join(directory, new_filename))
                    renamed_files.append(new_filename)
                    print(f"Renamed: {filename} to {new_filename}")
                else:
                    print(f"Skipping: {filename} (No title metadata)")
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")

    print("\nRenamed filenames array:")
    print(renamed_files)

def main():
    directory = "."  # You can change this to the desired directory
    update_filenames(directory)

if __name__ == "__main__":
    main()
