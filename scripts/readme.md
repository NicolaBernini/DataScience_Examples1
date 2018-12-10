
# Overview 

List of command lines and scripts to perform useful operations 

# Big CSV Split 

- Sometimes there is the need to work with CSV files which are too big and good way to deal with this is to split them 
- This can be performed with the Linux `split` command 
- Considering this is a CSV it can not be split looking just at the size as it could result in breaking one line, lines integrity need to be guaranteed 
  - the file break on the base of size is performed using the `bytes=1MB` option 
- the split on the base of lines will keep lines integrity 
  - the file break on the base of line is performed using the `-l 10000` option 

Example 

```
split -l 10000 ./target.csv ./target_chunks/target_chunk_
```
- This will break the large `target.csv` file into `N` files whose name starts with `./target_chunks/target_chunk_` and then a letters sequence extension is appended in order to get a unique filename 



