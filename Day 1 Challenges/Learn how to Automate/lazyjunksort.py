import os
import sys
import argparse
from pathlib import Path

# returns an arguement parser with "-p" arguement added
def create_arg_parser():
    parser = argparse.ArgumentParser(description='A simple python tool to sort your files!')
    parser.add_argument('-p', metavar="PATH", type=Path, required=True,  help='path to the directory to sort files from')
    return parser

if __name__ == "__main__":
    welcome = r'''
      ____.-.____
    [___________]
   (d|||||||||||b)
    `|||LAZY||||`
     |||JUNK||||
     |||SORT||||
     |||||||||||
     |||||||||||
     `"""""""""`
     '''
    print(welcome)

    directoryMappings = {
	"Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg", 
			".heif", ".psd",".jfif"], 
	"Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", 
			".qt", ".mpg", ".mpeg", ".3gp"], 
	"Documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", 
				".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", 
				".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", 
				"pptx", ".pdf", ".txt", ".pptx"],
	"Archives": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", 
				".dmg", ".rar", ".xar", ".zip"], 
	"Audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", 
			".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"], 
	"Exe": [".exe"], 
	"Shell": [".sh", ".bat"],
    "Programming": [".py", ".ipynb", ".html", ".sb3", ".htm"],
}
    
    # creates a dictionary of the format {extension:type} for eg. {".mp4":"Videos"}
    fileFormats = {file_format: directory 
				for directory, file_formats in directoryMappings.items() 
				for file_format in file_formats} 

    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:]) # just takes in the passed arguements removing the filename
    inputPath = parsed_args.p

    if os.path.exists(inputPath):
        for entry in os.scandir(inputPath):
            if entry.is_dir(): # if an item in the directory is a directory, it skips
                continue
            
            file_path = Path(entry) 
            file_format = file_path.suffix.lower() 
		    
            if file_format in fileFormats:
		# very confusing code but it basically 
		# it puts a file into its respective folder
		# if the folder doesn't exist, it makes a new one
		
                directory_path = Path(fileFormats[file_format])
                another_path = Path(os.path.join(Path(inputPath), directory_path))
                another_path.mkdir(exist_ok=True)
                newpath = os.path.join(inputPath, directory_path, file_path.name )
                file_path.rename(newpath)

	    # i have no clue why is this here...
            for dir in os.scandir(): 
                try: 
                    os.rmdir(dir)
                except: 
                    pass
        else:
            print(f"files from directory '{inputPath}' sorted")

    else:
        print("usage: lazyjunksort.py [-h] -p PATH\nlazyjunksort.py: error: invalid path")
