Prerequisites to run the 3 scripts.
1.)path is Kauai-Amakihi/Annotations/macaulay/tsv files for 1_tsvtocsv.py,  must create macaulay folder and tsv files subfolder
to hold Audacity generated .txt files that are in .tsv format by default (as of 10.27.25)
2.)create Kauai-Amakihi/Annotations/macaulay/csv files to hold output of 1_tsvtocsv.py
3.)create Kauai-Amakihi/Annotations/macaulay/reformatted files for 2_formatcsvs.py to place output files.
4.)adjust audio_folder in 2_formatcsvs.py to pathname of folder that holds audio clips, 2_formatcsvs.py adds a file column and
matches source file path+extension. 
5.)ensure audio_extensions in 2_formatcsvs.py is correct, by default it uses ['.wav','.m4a','.mp3'] but other projects might require other audio extensions
 be recognized by loop 
6.)adjust savepath in 3.concatcsvs.py to correct desired save location.

