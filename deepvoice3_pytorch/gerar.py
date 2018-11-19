import os
from os.path import exists, join, expanduser

import torch
import numpy as np
import librosa
import librosa.display
import IPython
from IPython.display import Audio
# need this for English text processing frontend
import nltk

checkpoint_path = "20171222_deepvoice3_vctk108_checkpoint_step000300000.pth"
preset = "./deepvoice3_vctk.json"

import hparams
import json

# Newly added params. Need to inject dummy values
for dummy, v in [("fmin", 0), ("fmax", 0), ("rescaling", False),
                 ("rescaling_max", 0.999),
                 ("allow_clipping_in_normalization", False)]:
  if hparams.hparams.get(dummy) is None:
    hparams.hparams.add_hparam(dummy, v)

# Load parameters from preset
with open(preset) as f:
  hparams.hparams.parse_json(f.read())

# Tell we are using multi-speaker DeepVoice3
hparams.hparams.builder = "deepvoice3_multispeaker"

# Inject frontend text processor
import synthesis
import train
from deepvoice3_pytorch import frontend
synthesis._frontend = getattr(frontend, "en")
train._frontend =  getattr(frontend, "en")

# alises
fs = hparams.hparams.sample_rate
hop_length = hparams.hparams.hop_size

def tts(model, text, p=0, speaker_id=0, fast=True, figures=True):
  from synthesis import tts as _tts
  waveform, alignment, spectrogram, mel = _tts(model, text, p, speaker_id, fast)
  if figures:
      visualize(alignment, spectrogram)
  # IPython.display.display(Audio(waveform, rate=fs))
  librosa.output.write_wav('out/speaker' + str(speaker_id) + '.wav', waveform, fs)

def visualize(alignment, spectrogram):
  label_fontsize = 16
  figure(figsize=(16,16))

  subplot(2,1,1)
  imshow(alignment.T, aspect="auto", origin="lower", interpolation=None)
  xlabel("Decoder timestamp", fontsize=label_fontsize)
  ylabel("Encoder timestamp", fontsize=label_fontsize)
  colorbar()

  subplot(2,1,2)
  librosa.display.specshow(spectrogram.T, sr=fs,
                           hop_length=hop_length, x_axis="time", y_axis="linear")
  xlabel("Time", fontsize=label_fontsize)
  ylabel("Hz", fontsize=label_fontsize)
  tight_layout()
  colorbar()

from train import build_model
from train import restore_parts, load_checkpoint
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output_directory', type=str,
                        help='directory to save checkpoints')
    parser.add_argument('-t', '--text', type=str, default=None,
                        required=False, help='text to synthetize')

    args = parser.parse_args()

    model = build_model()
    model = load_checkpoint(checkpoint_path, model, None, True)

    # Try your favorite senteneces:)
    text = "Some have accepted this as a miracle without any physical explanation"
    if args.text is not None:
        text = args.text
    N = 15
    print("Synthesizing \"{}\" with {} different speakers".format(text, N))
    for speaker_id in range(N):
      print(speaker_id)
      tts(model, text, speaker_id=speaker_id, figures=False)
