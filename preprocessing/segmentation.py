import os
import sys
import ntpath
import cv2

import segment_sentence
import segment_word
import segment_character
import augment

file = sys.argv[1] # Get file name from parameter
fileName = filename = os.path.splitext(file)[0] # Take name of file without extension
directory = 'Segmented_' + os.path.splitext(ntpath.basename(file))[0] # Generate directory name to store segmented images

# Check if subfolder already exists. If it doesn't, create it
if not os.path.exists(directory):
	os.makedirs(directory)

# Read the image as numpy array
image = cv2.imread(file)
s=0
# Get sentences as separate images
sentences = segment_sentence.segment_sentence(image)

for i in range(0,len(sentences)):
	# Get words as separate images
	words = segment_word.segment_word(sentences[i])
	s+=1
	w=0
	for j in range(0,len(words)):
		# Get characters as separate images
		characters = segment_character.segment_character(words[j])
		w+=1
		c=0
		for k in range(0,len(characters)):
			c+=1
			""" 
				Generate image name based on position in original image
			 	Format is LL-WW-CC where
			 		LL is line number
			 		WW is word number in LL
			 		CC is character number in WW
			 """
			imageName = str(s).zfill(2) + '-' + str(w).zfill(2) + '-' + str(c).zfill(2) + '.png'

			# save image
			cv2.imwrite(os.path.join(directory, imageName), characters[k])

augment.augment(directory)


