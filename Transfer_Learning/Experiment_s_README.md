# **Experiment Details for Transfer Learning **
## Experiment 1s
- All data was the same as experiment 4 from deep learning 
- Trained on 3 second clips with 1.5 second overlap
- pretty mediorcre performance
## Experiment 2s
- Botched experiment
- No embeddings
- Poor performance
## Experiment 3s
- Increased clip length to 5 seconds, 2.5 second overlap, 0.25 min overlap for training
- Validation remained at 3 seconds.
- *AT THIS POINT, WE REALIZED THAT THE TRAINING AND VALIDATION SETS CONTAINED UNCERTAIN ANNOTATIONS (e.g ?KAAM_song)
## Experiment 4s
- No uncertain clips, addition of AKEK and ANIA XC mp3s & 3000 random XC clips as negatives in training
    - We realized that we had done audio_files = valid["audio_file"].unique() during clip generation in deep learning and transfer learning up to this point, which provides *less* audio files than actually present. all audiofiles with no annotations do not get considered for boxes and then clips.
- validation set was the same with the exception of uncertain annotation clips
## Experiment 5s
- Addition of more annotations in training set (macaulay .m4a's, which were not included before, annotated and added to set)
- Training set comprised of AKEK and ANIA XC mp3s clips, 3000 random XC clips, KAAM focal clips (with new .m4a's)
- Still poor performance on validation set. Potential incorrect annotations (negatives that should be positives) in validation set, which need to be reviewed and potentially reannotated.