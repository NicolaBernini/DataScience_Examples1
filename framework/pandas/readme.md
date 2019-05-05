
# Overview 

Some Example related to Pandas Framework 

# Operations 

## Basic Operations 

### Column Rename 

- It is not possible to change a single column name directly via the `df.columns` attribute, in fact doing something like 

```python 
df.columns[0] = 'Test'
```

results in a `TypeError("Index does not support mutable operations")`

however it is possible to modify the full set as follows 

```python 
temp=df.columns.values
temp[0] = 'Test'
df.columns = temp
```



Work in progress 

