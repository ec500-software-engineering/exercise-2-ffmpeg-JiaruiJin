# EC500 exercise 2 - Asynchronous Video Encoding
  Learned to :  
  1. Managing number of workers : **queue**  
  2. Multiprocessing and multithreading  
  3. Unit test: pytest -> **test_duration.py**
## Prerequisite
  Python3.7  
  ffmpeg
## Instruction
  Change the path in **main.py**  
  put the **videoplayback.mp4** in the same path  
  run **main.py** to get converted video documents  
  use the 480p video to compare with original video in duration
## CPU evaluation
  ![](https://github.com/ec500-software-engineering/exercise-2-ffmpeg-JiaruiJin/blob/master/CPU_Evaluation.PNG)  
  The cpu of my computer is Intel i7-8550U with the Memory Size of 16GB. By running **main.py** two **ffmpeg** function will make up about  
  286.1MB.  
  16GB/286.1MB ≈ 55.9 -> maximum number around 55. 

