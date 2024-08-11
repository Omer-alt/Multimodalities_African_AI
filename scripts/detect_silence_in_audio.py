import os
import re
import subprocess
import downloader
import errno

def detect_silence(input_file, silence_threshold='-50dB', silence_duration=1):
    command = [
        'ffmpeg', '-i', input_file,
        '-af', f'silencedetect=noise={silence_threshold}:d={silence_duration}',
        '-f', 'null', '-'
    ]
    result = subprocess.run(command, stderr=subprocess.PIPE, text=True)
    return result.stderr

def parse_silence_output(output):
    silence_start = []
    silence_end = []

    for line in output.split('\n'):
        start_match = re.search(r'silence_start: (\d+(\.\d+)?)', line)
        end_match = re.search(r'silence_end: (\d+(\.\d+)?)', line)

        if start_match:
            silence_start.append(float(start_match.group(1)))
        if end_match:
            silence_end.append(float(end_match.group(1)))

    return silence_start, silence_end

def split_audio(input_file, start_times, end_times, output_directory, output_prefix='output'):
    prev_end = 0
    segment = 1
    durations = []
    for start, end in zip(start_times, end_times):
        duration = start - prev_end
        if duration < .5:
            continue
        output_file =  f'{output_directory}/{output_prefix}_{segment}.mp3'
        command = [
            'ffmpeg', '-i', input_file,
            '-ss', str(prev_end), '-t', str(duration),
            '-c', 'copy', output_file
        ]
        subprocess.run(command)
        prev_end = end
        segment += 1

    # Handle the last segment
    # try:
        # os.mkdir(output_directory)
    print("\n\noutput_directory : \n\n", output_directory)
    os.makedirs(output_directory, mode = 0o777, exist_ok = True) 
    # except OSError as e:
    #     print(e.errno.__str__)
    #     if e.errno != errno.EEXIST:
    #         raise
    output_file = f'{output_directory}/{output_prefix}_{segment}.mp3'
    command = [
        'ffmpeg', '-i', input_file,
        '-ss', str(prev_end),
        '-c', 'copy', output_file
    ]
    subprocess.run(command)
    print(durations)


def extract(category:str):
    for b in downloader.allBooks[category]:
        for chi in range(16, downloader.allBooks[category][b]+1):
            b= b.replace(" ", "_")
            
            chapterString = ""
            if chi <= 9:
                chapterString = f"0{chi}"
            else:
                chapterString = f"{chi}"
            ch = f"Ch_{chapterString}.mp3"
            input_file = f"{category}/{b}/{ch}"
            silence_threshold = '-40dB'
            silence_duration = 1 # 1-second.

            silence_output = detect_silence(input_file, silence_threshold, silence_duration)
            start_times, end_times = parse_silence_output(silence_output)

            if len(start_times)==0:
                continue
            dChapter = ch.lower().split(".")[0]
            split_audio(input_file, start_times, end_times, f"Splitted/{category}/{b}/{dChapter}",f'{b.lower()}_{dChapter}')
            break
        break

if __name__ == '__main__':
    extract("OldTestament")
    # extract("NewTestament")
