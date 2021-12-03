GREEN="$(printf '\e[32m')"
CYAN="$(printf '\e[36m')"
clear
echo "$CYAN              Created by SHAURYA MISHRA"
sleep 1
clear
echo "$GREEN   Initiating Server."
sleep 1
clear
echo "$GREEN   Initiating Server.."
sleep 1
clear
echo "$GREEN   Initiating Server..."
sleep 2
echo """//
// writewav.c - Create a wav file by piping raw samples to ffmpeg
// Written by Ted Burke - last updated 10-2-2017
//
// To compile:
//
//    gcc writewav.c -o writewav -lm
//
 
#include <stdio.h>
#include <stdint.h>
#include <math.h>
 
#define N 44100
 
void main()
{
    // Create audio buffer
    int16_t buf[N] = {0}; // buffer
    int n;                // buffer index
    double Fs = 44100.0;  // sampling frequency
     
    // Generate 1 second of audio data - it's just a 1 kHz sine wave
    #for (n=0 ; n<N ; ++n) buf[n] = 16383.0 * sin(n*1000.0*2.0*M_PI/Fs);
     
    #// Pipe the audio data to ffmpeg, which writes it to a wav file
    #FILE *pipeout;
    ipeout = popen("ffmpeg -y -f s16le -ar 44100 -ac 1 -i - beep.wav", "w");
    #3fwrite(buf, 2, N, pipeout);
    #pclose(pipeout);
  """		 
sleep 1
bash anonymousbomber.sh
