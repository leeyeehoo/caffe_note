# caffe_note
To write data into lmdb:  
```python
if vector.dtype == np.int:
datum.data = vector.tostring()
elif vector.dtype == np.float:
datum.float_data.extend(vector.flat)
```
To read int data in lmdb:  
```python
flat_x = np.fromstring(datum.data, dtype=np.int)
x = flat_x.reshape(datum.channels, datum.height, datum.width)
y = datum.label
```
To read float data in lmdb:
```python
x = np.array(datum.float_data).astype(float).reshape( datum.channels, datum.height, datum.width)
y = datum.label
```
