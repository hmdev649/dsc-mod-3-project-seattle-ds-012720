def pickle_it(model_name):
    import pickle
    
    output_file = open('../../src/pickles/{}_classifier.pickle'.format(type(model_name).__name__), 'wb')
    pickle.dump(model_name, output_file)
    output_file.close()
    
    print('I Kid You Not Jeff, He Turns Himself Into a Pickle')
    pass