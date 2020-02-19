# Vela Pulsar Data Analysis and Spectrogram

Data is taken from **Ooty observations on the Vela pulsar (taken during CHERA 2015)**<br>
Data contains time-series volages of North-Half and South-Half Telescope , sampled with frequency of **16.5 MHz** <br>

### Code for the Dynamic Spectrum and Histogram : 

- Importing Numpy Library Storing data of `vela_Pulsar.mbr` into `data1` and Dividing data into North Half and South Half data:
```python
import numpy as np
data1 = np.loadtxt('vela_Pulsar.mbr')
 
north_data = data1[:,[0]]
south_data = data1[:,[1]]
north_data = np.array(north_data,dtype = complex)
south_data = np.array(south_data,dtype = complex)
```
- Resizing the `north_data` and `south_data` to 512 x 60000(column wise) to get frequency spectrum of given data :
```python
north_data = np.reshape(north_data,(512,60000),order = 'F')
south_data = np.reshape(south_data,(512,60000),order = 'F')
```
- Now getting Fourier-Transform of all columns of `north_data` and `south_data` and getting their square of absolute values :
```python
for i in range(0,len(north_data[0])):
    north_data[:,i] = np.power(np.abs(np.fft.fft(north_data[:,i])),2)
    south_data[:,i] = np.power(np.abs(np.fft.fft(south_data[:,i])),2)
```
- Now Reducing the **Noise(gaussian)** and also getting reqiured **time-resolution** :
```python
north_fft = np.zeros((512,1000))
south_fft = np.zeros((512,1000))
for i in range(0,1000):
    north_fft[:,i] = np.sum(np.real(north_data[:,60*i:60*(i+1)-1]),axis = 1)
    south_fft[:,i] = np.sum(np.real(south_data[:,60*i:60*(i+1)-1]),axis = 1)
```
- Plotting the Matrix of `north_fft` and `south_fft` using `matplotlib` Library , where column number correspondes to __frequency__ and row number corresponds to __time__ :

```python
from matplotlib import pyplot as plt
ax1 = plt.matshow(north_fft[256:511,:])
ax2 = plt.matshow(south_fft[256:511,:])
```
1. North Half Data Spectrogram :
<br>
![North Half Data](https://github.com/Devansh0210/TRAC-Assignments/blob/master/TRAC%202020%20task/north.png?raw=true)

2. South Half Data Spectrogram : 
<br>
![South Half Data](https://github.com/Devansh0210/TRAC-Assignments/blob/master/TRAC%202020%20task/south(1).png?raw=true)
