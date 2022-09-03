import pip
import sys
import os
import platform
# os.environ["OMP_NUM_THREADS"] = "1" # export OMP_NUM_THREADS=1
# os.environ["OPENBLAS_NUM_THREADS"] = "1" # export OPENBLAS_NUM_THREADS=1
# os.environ["MKL_NUM_THREADS"] = "1" # export MKL_NUM_THREADS=1
# os.environ["VECLIB_MAXIMUM_THREADS"] = "1" # export VECLIB_MAXIMUM_THREADS=1
# os.environ["NUMEXPR_NUM_THREADS"] = "1" # export NUMEXPR_NUM_THREADS=1

import math
import subprocess
from multiprocessing import Pool, cpu_count
import psutil
import resource
  
# def memory_limit(percentage: float):
   
#     if platform.system() != "Linux":
#         print('Only works on linux!')
#         return
#     soft, hard = resource.getrlimit(resource.RLIMIT_AS)
#     resource.setrlimit(resource.RLIMIT_AS, (get_memory() * 1024 * percentage, hard))

# def get_memory():
#     with open('/proc/meminfo', 'r') as mem:
#         free_memory = 0
#         for i in mem:
#             sline = i.split()
#             if str(sline[0]) in ('MemFree:', 'Buffers:', 'Cached:'):
#                 free_memory += int(sline[1])
#     return free_memory

# def memory(percentage=0.8):
#     def decorator(function):
#         def wrapper(*args, **kwargs):
#             memory_limit(percentage)
#             try:
#                 return function(*args, **kwargs)
#             except MemoryError:
#                 mem = get_memory() / 1024 /1024
#                 print('Remain: %.2f GB' % mem)
#                 sys.stderr.write('\n\nERROR: Memory Exception\n')
#                 sys.exit(1)
#         return wrapper
#     return decorator

# memory(percentage=0.5)




# subprocess.check_call([sys.executable, '-m', 'pip', 'install','transformers'])
# subprocess.check_call([sys.executable, '-m', 'pip', 'install','librosa'])
# subprocess.check_call([sys.executable, '-m', 'pip', 'install','torch'])

import librosa
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

#load pre-trained model and tokenizer
tokenizer = Wav2Vec2Tokenizer.from_pretrained("Harveenchadha/vakyansh-wav2vec2-indian-english-enm-700")
model = Wav2Vec2ForCTC.from_pretrained("Harveenchadha/vakyansh-wav2vec2-indian-english-enm-700")

import os
dir_list = os.listdir("/home/rohit/Documents/New Folder/file/L_mp3/waves/")
#print(dir_list)
n =0
file_name = "text_1.txt"
wfile = open(file_name, 'w+', encoding='utf-8')
count = 6
for x in dir_list:
    if x.endswith(".wav"):
        count += 1
    else:
        continue
    speech, rate = librosa.load(x,sr=16000)
    input_values = tokenizer(speech, return_tensors = 'pt').input_values
    #Store logits (non-normalized predictions)
    logits = model(input_values).logits
    #Store predicted id's
    predicted_ids = torch.argmax(logits, dim =-1)
    #decode the audio to generate text
    transcriptions = tokenizer.decode(predicted_ids[0])
    wfile.write(x+"\t"+transcriptions+"\n")
    print(psutil.Process().memory_info().rss / (1024 * 1024))
    # print(x,";",transcriptions)
    n += 1
print(n)
print(count)