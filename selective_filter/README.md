## Real-Time Selective Noise Filter: Version 1

This code allows one to record a noise they don't want to hear, and their headphones will filter that sound out for them while allowing the approved sounds through. Potential uses: listening in lectures where other students may be typing a lot; in a cafe where you like the music playing but not a certain sound (might be a little difficult to record that sound...); etc. 

This is a work-in-progress. 

The real-time functionality is achieved via <a href="https://github.com/bastibe/SoundCard">SoundCard</a>. (see LICENSE_SoundCard)

## Set Up

1) Clone the repository

2) Set working directory as '.../real-time-applications/selective_filter', i.e. where this README file lives. 

3) Set up a virtual environment:

```
$ python3 -m venv env
$ source env/bin/activate
(env)..$ 
```
If you don't have venv installed:
```
$sudo apt-get install python3-venv
```
Then repeat the steps mentioned above.

4) Install the requirements.

```
(env)..$ pip install -r requirements.txt
```

5) run the program!

It will ask you to press 'Enter' when you are ready to record the background noise you would like to filter out. This will record for 5 seconds. Then it will apply a filter reducing that noise, real-time, with a 2 second delay. You can hear this new noise reduced environment through your headphones.

```
(env)..$ python3 realtime_filter.py
```

## Next Steps

1) Improve the filter. I am working on implementing a Wiener filter.

2) Include postfilter. I would like to implement a postfilter that reduces the musical noise, which results from initial filtering.

3) Decrease latency. Right now the latency is around 2 seconds; I would like to reduce this for potential use in conversational settings. 
