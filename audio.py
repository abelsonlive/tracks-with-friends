
from util import run_cmd 


def extract_metadata(tmp_filepath):
    args = [
      'ffprobe', '-v', 'quiet', '-print_format', 'json', '-show_format', 
      '-show_streams', tmp_filepath
    ]
    return run_cmd(*args, json=True)

if __name__ == '__main__':
  print(extract_metadata('/Users/brianabelson/Desktop/SURF DUDE_202562981_soundcloud.mp3'))