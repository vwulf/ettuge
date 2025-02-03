# ~/code/ettuge/src/main/md/kannada 
cat sections/list_of_files.txt | grep -v "#" | xargs pandoc -r gfm -w gfm -o Eke-1.md
