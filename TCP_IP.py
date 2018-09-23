from multiprocessing import process
import  MiddlleMan
import TCP_manager
import numpy as np

def start():
    com_manager = TCP_manager.TcpManagerClass()

    while True:
        print("tcp_ip process is running")
        ###################################### Listening ####################################################################
        request = com_manager.TCP_listener()
        print(request)
        ##################################### End listerning ################################################################

        ##################################### Send requested data to master #################################################

        # It should be something like this

        # middle_man = middleman.class_name()
        # response = middle_man.get(command=request)

        #### But, Just demo (response) to remove ###################
        array = np.round(np.random.rand(2, 2))
        arr_str = np.array2string(array)  # Generating some random numpy array and sending it as string as demo
        print(arr_str)
        ################# Demo end ####################

        com_manager.TCP_send(arr_str)  # send response
