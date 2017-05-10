# Lessons

This file serves to record some of the dev related things that I have learned 
while working on this project.
I would like the project descriptions to focus only on the solution at hand 
but I ran into issues where
I wanted to record information related to my general dev environment.  
This file will serve as that repository.
My main IDE is PyCharm 2016 but I occasionally use a Jupyter Notebook.

## Unittests

Learn.

## Code Templates

Code templates are a useful feature for quickly creating a code skeleton for 
a new project.  I created a `skeleton`
folder to ease this process for when I work in a bash shell but I was curious 
to see if I could add the 
[code templates](https://www.jetbrains.com/help/pycharm/2017.1/file-and-code-templates.html) 
I made explicitly to the
project configuration files so that I could share them between my different 
environments.  This is performed 
by changing the schema to "project" before creating the templates.  This 
adds the templates into 
`.idea/fileTemplates/` and the files can be version controlled from there.

Code templates are written in 
[Velocity](http://velocity.apache.org/engine/1.7/vtl-reference.html). 
I ran into
the issue where Velocity was reading Markdown sub-headers as comments.  
Use `#[[ unparsed content ]]#` to 
render content at runtime rather than interpreting it. 

## .idea Directory

I became interested in wondering how I could share my project configuration 
between my different computers
(when I realized that I needed to mark source roots for unittests).  The 
project's [.idea](https://www.jetbrains.com/help/pycharm/2017.1/project.html) 
folder contains this
configuration but JetBrain's 
[post](https://intellij-support.jetbrains.com/hc/en-us/articles/206544839) about
how to manage this directory under source is lacking.  The issue is that 
some files maintain information about local
configuration(Python interpreter) while others do not(source roots).  
Github provides a nice 
[.gitignore](https://github.com/github/gitignore/blob/master/Global/JetBrains.gitignore)
example but I think that it is high time that I document for myself 
what the various files in this directory do.

### Ignore

* `dictionaries/` - store saved words to a local dictionary.  Not added to 
    a shared project dictionary to 
    avoid conflicts.
* `dataSources/` - database stuff.  In earlier versions(< 14) sensitive 
    database passwords were stored here.

### Add

* `fileTemplates/` - Stores code templates
* `runConfigurations/` - Stores run configurations. Make sure the interpreter 
    is set to the project default so that
    it is possible to different interpreters on each platform, without 
    changing the settings every time.
* `inspectionProfiles/` - Stores 
    [inspection profiles](https://www.jetbrains.com/help/idea/2017.1/code-inspection.html#profiles).
    I have not used these.
* `modules.xml` - references project libraries.  In PyCharm, modules are to a 
    project what projects are to a solution
    in Visual Studio.
* `*.iml` files in `.idea/*` - 
    [Module library](http://www.jetbrains.org/intellij/sdk/docs/basics/project_structure.html).
    Contains information about each module. Share a local name for 
    the project interpreter.  The configuration for the interpreter can be 
    different between platforms but the
    name must be shared so that the module library file does not change every 
    time a different interpreter is used.

## Lessons

* I had an issue adding sub-headers in code templates for Markdown files.  It 
    looks like `#` is some sort of 
    reserved keyword and two of them commented out the rest of the line.
* In Pycharm, make sure to add directories to the source root to `import` 
    local scripts.
* Use a conda environment when possible.  I prefer conda's `environment.yml` 
    over `requirements.txt` since
    it explicitly details what version of python the project is using.
* Share a project interpreter name when sharing `.idea` file.