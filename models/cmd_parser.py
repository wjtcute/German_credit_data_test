def TrainTestFileParser(argv,num=None):
    'argv = the whole sys.argv; num = the number of the pair of train and test set'

    if (num==None): num = ''
    else: num = str(num)

    argl = len(argv)

    if (argl<=1):
        train_data_file = "../data/features_numeric_train"+num+".txt"
    else:
        train_data_file = argv[1]

    if (argl<=2):
        test_data_file = "../data/features_numeric_test"+num+".txt"
    else:
        test_data_file = argv[2]

    if (argl<=3):
        test_result_dir = "../data/"
    else:
        test_result_dir = argv[3]

    return (train_data_file,test_data_file,test_result_dir)
