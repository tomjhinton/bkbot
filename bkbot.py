from textgenrnn import textgenrnn
textgen = textgenrnn('textgenrnn_weights.hdf5',vocab_path='textgenrnn_vocab.json',
config_path='textgenrnn_config.json')

#textgen = textgenrnn()
#textgen.train_from_file('bktestform3.csv', num_epochs=5, new_model=True)
textgen.generate_to_file('Ne3.csv', n=500)
