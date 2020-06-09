with open ('K.R.Venkhat_Balaji.jpg','rb') as rf:
    with open ('K.R.Venkhat_Balaji_copy.jpg','wb') as wf:
        file_size = 4096
        rf_size = rf.read(file_size)
        while len (rf_size) > 0:
            wf.write(rf_size)
            rf_size = rf.read(file_size)
