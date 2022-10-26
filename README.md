# Introduction
Use multiprocessing.Pool to train your model asynchronously.  
Please make sure that the path in ```sys.path.append("path to where you stored check_gpu_workable script")``` is changed correctly.  
```check_gpu_workable.py``` can be found [here](https://github.com/EpicTian/check_gpu_available).

# Requirements
```shell
pip3 install multiprocess
```
or
```shell
conda install multiprocess
```

# Usage
Code the ```async_train.py``` to suit your task then run the following code in your SSH terminal:
```shell
nohup ./async_train.py > ./nohup_output.log 2>&1 &
```
