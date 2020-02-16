
import numpy as np
data1 = np.loadtxt('vela_Pulsar.mbr')


north_data = data1[:,[0]]
south_data = data1[:,[1]]
north_data = np.array(north_data,dtype = complex)
south_data = np.array(south_data,dtype = complex)


north_data = np.reshape(north_data,(512,60000),order = 'F')
south_data = np.reshape(south_data,(512,60000),order = 'F')


for i in range(0,len(north_data[0])):
    north_data[:,i] = np.power(np.abs(np.fft.fft(north_data[:,i])),2)
    south_data[:,i] = np.power(np.abs(np.fft.fft(np.reshape(south_data[:,[i]],(1,512)))),2)

north_fft = np.zeros((512,1000))
south_fft = np.zeros((512,1000))
for i in range(0,1000):
    north_fft[:,i] = np.sum(np.real(north_data[:,60*i:60*(i+1)-1]),axis = 1)
    south_fft[:,i] = np.sum(np.real(south_data[:,60*i:60*(i+1)-1]),axis = 1)


from matplotlib import pyplot as plt
plt.imshow(north_fft[0:255,:]);
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.colorbar()
plt.show()


from matplotlib import pyplot as plt
plt.imshow(south_fft[0:255,:]);
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.colorbar()
plt.show()


hist_north = data1[:,[0]]
plt.hist(hist_north,bins = 350)
plt.show()


hist_south = data1[:,[1]]
plt.hist(hist_north,bins = 350)
plt.show()
