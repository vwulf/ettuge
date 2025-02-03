# ~/code/ettuge/src/main/md/kannada 
cat sections/list_of_files.md | grep -v "#" | xargs pandoc -r gfm -w gfm -o Eke-1.md
