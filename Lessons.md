# Lessons

This file serves to record some of the dev related things that I have learned while working on this project.
I would like the project descriptions to focus only on the solution at hand but I ran into issues where
I wanted to record information related to my general dev environment.  
This file will serve as that repository.
My main IDE is PyCharm 2016 but I occasionally use a Jupyter Notebook.

## Unittests

Learn.

## .idea

I became interested in wondering how I could share my project configuration between my different computers
(when I realized that I needed to mark source roots for unittests).  The project's [.idea](https://www.jetbrains.com/help/pycharm/2017.1/project.html) folder contains this
configuration but JetBrain's [post](https://intellij-support.jetbrains.com/hc/en-us/articles/206544839) about
how to manage this directory under source is lacking.  The issue is that some files maintain information about local
configuration(Python interpreter) while others do not(source roots).  Github provides a nice [.gitignore](https://github.com/github/gitignore/blob/master/Global/JetBrains.gitignore)
example but I think that it is high time that I document for myself 
what the various files in this directory do.



## Lessons

* I had an issue adding sub-headers in code templates for Markdown files.  It looks like `#` is some sort of 
    reserved keyword and two of them commented out the rest of the line.
* In Pycharm, make sure to add directories to the source root to `import` local scripts.
* Use a conda environment when possible.  I prefer conda's `environment.yml` over `requirements.txt` since
    it explicitly details what version of python the project is using.