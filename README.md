Calibre Google Drive Fix
==================

Restores ebook directories with their Calibre IDs, originally removed by Google Drive. 

## The problem

Calibre requires a specific directory structure that uses parentheses in the book's directory name, for example
 
     The Martian (317)
     
Google Drive, however, has a [bug](https://productforums.google.com/forum/#!searchin/drive/rename/drive/XJzVGC868DQ%5B1-25-true%5D), it does not like parentheses in directory names, and so the above ends up in Google Drive as

    The Martian
    
The next time you sync your ebooks on a new machine, you don't get the parentheses back. 
Calibre will list your books nicely, but is unable to find the actual folder.

## This script

This script fixes the problem by renaming the folders back to what Calibre expects. 

To use it, 

    python gdrivefix.py
    
You will be prompted to enter the path to your ebooks directory.  The script goes through and renames the directories to their numbered versions.

## Notes

You would normally run this script once on each new install.  After that you don't need it.
  
Just in case, do make a backup of your ebooks directory before you run it.
 
This has only been tested on Ubuntu 14.04 with Python 2.7.  It should work as long as you have Python 2.x. 





