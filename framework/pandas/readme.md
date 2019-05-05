
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



### Function Application 

To a Series 

```python 
df["ColName"].apply(f)
```

To a DataFrame, it is possible to decide whether to pass rows or cols hence to iterate over the other dimension 

To iterate over cols hence passing rows as args just use the default `axis=0` value 

```python 
df.apply(f)
```

To iterate over the rows hence passing cols as args 

```python 
df.apply(f, axis=1)
```

Work in progress 

