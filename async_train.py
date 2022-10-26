import sys 
sys.path.append("path to where you stored check_gpu_workable script")
from check_gpu_workable import gpu_workable
import torch
from multiprocessing import Pool



def main(train_data, device_id, lr):
    model = Model().to(device_id)
    optimizer = torch.optim.Adam(model.parameters(), lr = lr)
    pass



def err_call_back(err):
    print(f'Error：{str(err)}')



if __name__ == '__main__':
    # An example of using multiprocessing.Pool
    # Create a pool containing num child processes.
    num = 7
    pool = Pool(processes = num)
    i = 0
    for lr_ in (1e-2, 1e-3, 1e-4):
        # Get the GPU ID with the available GPU memory usage greater than or equal to 50.00% (default).
        gpuid = gpu_workable()
        device = torch.device("cuda:"+str(gpuid) if torch.cuda.is_available() else "cpu")
        # Must assign every parameter of main() one-to-one correspondence.
        pool.apply_async(main, args=(traindata, device, lr_), error_callback=err_call_back)
        i += 1
        print('====== Process[{}] apply_async {}  ======'.format(os.getpid(),i))
    # No new child process assigned into the pool after close().
    pool.close()
    # Wait for all child process in the pool to finish.
    pool.join()
    print('Mainprocess is end.')
