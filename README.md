# Real-Time Voice Cloning Web Application (Flask Implementation)
This repository is an implementation of [Transfer Learning from Speaker Verification to
Multispeaker Text-To-Speech Synthesis](https://arxiv.org/pdf/1806.04558.pdf) (SV2TTS) with a vocoder that works in real-time. Feel free to check [my thesis](https://matheo.uliege.be/handle/2268.2/6801) if you're curious or if you're looking for info I haven't documented. Mostly I would recommend giving a quick look to the figures beyond the introduction.

SV2TTS is a three-stage deep learning framework that allows to create a numerical representation of a voice from a few seconds of audio, and to use it to condition a text-to-speech model trained to generalize to new voices.

**Video demonstration** (click the picture):

[![Modiefied Toolbox demo](https://i.ytimg.com/vi/rBttZhhYXBA/hqdefault.jpg)](https://www.youtube.com/watch?v=rBttZhhYXBA)



### Papers implemented  
| URL | Designation | Title | Implementation source |
| --- | ----------- | ----- | --------------------- |
|[**1806.04558**](https://arxiv.org/pdf/1806.04558.pdf) | **SV2TTS** | **Transfer Learning from Speaker Verification to Multispeaker Text-To-Speech Synthesis** | This repo |
|[1802.08435](https://arxiv.org/pdf/1802.08435.pdf) | WaveRNN (vocoder) | Efficient Neural Audio Synthesis | [fatchord/WaveRNN](https://github.com/fatchord/WaveRNN) |
|[1712.05884](https://arxiv.org/pdf/1712.05884.pdf) | Tacotron 2 (synthesizer) | Natural TTS Synthesis by Conditioning Wavenet on Mel Spectrogram Predictions | [Rayhane-mamah/Tacotron-2](https://github.com/Rayhane-mamah/Tacotron-2)
|[1710.10467](https://arxiv.org/pdf/1710.10467.pdf) | GE2E (encoder)| Generalized End-To-End Loss for Speaker Verification | This repo |

## News
**11/01/21**: Result save support added.


**13/11/19**: I'm now working full time and I will not maintain this repo anymore. To anyone who reads this:
- **If you just want to clone your voice (and not someone else's):** I recommend our free plan on [Resemble.AI](https://www.resemble.ai/). Firstly because you will get a better voice quality and less prosody errors, and secondly because it will not require a complex setup like this repo does.
- **If this is not your case:** proceed with this repository, but be warned: not only is the environment a mess to setup, but you might end up being disappointed by the results. If you're planning to work on a serious project, my strong advice: find another TTS repo. Go [here](https://github.com/CorentinJ/Real-Time-Voice-Cloning/issues/364) for more info.

**20/08/19:** I'm working on [resemblyzer](https://github.com/resemble-ai/Resemblyzer), an independent package for the voice encoder. You can use your trained encoder models from this repo with it.

**06/07/19:** Need to run within a docker container on a remote server? See [here](https://sean.lane.sh/posts/2019/07/Running-the-Real-Time-Voice-Cloning-project-in-Docker/).

**25/06/19:** Experimental support for low-memory GPUs (~2gb) added for the synthesizer. Pass `--low_mem` to `demo_cli.py` or `demo_toolbox.py` to enable it. It adds a big overhead, so it's not recommended if you have enough VRAM.


## Setup

### 1. Install Requirements

**Python 3.6 or 3.7** is needed to run the toolbox.

* Install [PyTorch](https://pytorch.org/get-started/locally/) (>=1.0.1).
* Install [ffmpeg](https://ffmpeg.org/download.html#get-packages).
* Run `pip install -r requirements.txt` to install the remaining necessary packages.
* Also install Flask with pip using command `pip install Flask`
### 2. Download Pretrained Models
Download the latest [here](https://github.com/CorentinJ/Real-Time-Voice-Cloning/wiki/Pretrained-models).

### 3. Run The Server
Run the server by following given command.

`python server.py`

### 4. Upload Audio
Upload the audio mp3 or wav file, for which you want to create an utterance.


### 5. Type Text
Type the text for which you want to create audio..


### 6. Click Upload
Click on Upload Button.


### 7. Listen The Difference.
Listen The Difference Between Two Audios Enjoy It.


### 8. Enjoy. Note
Do Not Abuse this code.
Never click upload button without audio selection and text. I give unexpected outputs.
