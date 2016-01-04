PROJECT TEMPLATE USING PYTHON
=
Scientific projects often require the same folders and files. Starting each new project with a standard folder and file structure helps researchers stay organised. This can help  collaborators find and work with project files, as well as help make a project more reproducible.

At present, this project template will not be appropriate for all scientific projects. Looking on the web, there are several other examples of project templates, but in my experience these are often aimed at people who work primarily with big data, modelling, or some form of software-based science. Scientists in these fields usually already know the benefits of version control, data integrity, file organisation and code testing. 

My project template is aimed at scientists that use computers as part of their research, but who do not consider themselves computer scientists or computer experts. My own experience lies in the life and health sciences, where many researchers have little to no training in computer programming, and the use of Excel and other error prone and irreproducible software suites is rampant. The use of a standard template and an introduction to an alternative way of working (e.g., version control, text files, LaTeX, writing computer code) may help us, the scientists who work in these varied fields, integrate some of the important lessons that computer science and related disciplines have learned a long time ago.

Usage
--
To run the main function and create a project template (files and folders described below), simply run:
> $ python project.py < base > < project >

< base>  = Folder where main project folder will be created; e.g., /home/martin/Documents/
< project > = Name of project; this will be the name of the main folder; e.g., cool_project
Note that you should not use quotation marks on the command line.

> $ python project.py /home/martin/Documents/ cool_project

The above command would create a project template called `cool_project`; the folder would be located in `/home/martin/Documents/`
 
The function has been tested with Python >2.7  or Python >3.4. 

Folder Structure
--
The basic structure is to keep source documents (`src`), data (`data`), and generated documents (`doc`) in separate folders. 

Lets pretend our project is called "zombie_brain". Running the main function from the command line generates the following folder structure:

* `zombie_brain` 
    * `src`
        * `code`
            * `data_proc`
            * `fig_gen`
            * `stats`
        * `notes`
        * `ms`
		* `ethics`
		* `slides`
		* `protocol`
		* `results`
	* `data`
        * `raw`
        * `proc`
    * `doc`
        * `notes`
        * `ms`
		* `ethics`
			* `scans`
		* `slides`
		* `protocol`
		* `results`
		* `misc`
		
src
--

All the code and text you write will be located in one location, which will make it easy to use version control software to keep track of your work. Therefore, you will want to keep most of your work in this folder because you will be able, if you use simple text-based files, to revert to all the previous versions of any document. You will also be able to compare the changes between two different versions of a document. 

Code written to process data should be located in the `code` subfolder. This code can be written in any programming language (e.g., Matlab, Python, R). Currently, the `code` folder contains three subfolder, `data_proc`, `fig_gen` and `stats`. Additional folders and subfolder can be added depending on the nature of the project.

It is assumed that projects notes and manuscript(s) will be written using LaTeX. This is advisable because .tex files are simple text files that are easy to use with version control software. Tracking your work and the various versions of your notes and manuscripts become more complicated if you use .odt (LibreOffice) or .docx (Microsoft Office).

While LaTeX is not supported by all scientific journals, especially in the life sciences, it is still a good idea to draft your manuscript in LaTeX. An alternative is to write your manuscript using simple Markdown language; the disadvantage is that entering your references by hand can be a little tedious and error prone. If you consider the amount of time you spend writing and revising a manuscript --especially if you are the primary author-- it is very little effort to do a final cut-and-paste into a LibreOffice or Word and finalise the formatting there.

To facilitate things, the `notes` and `ms` (manuscript) folders are initialised with a LaTeX template for notes and a manuscript. Obviously, some familiarity with LaTeX is required in order to use and compile these documents. 

Other folders that are included in the `src` folder are `ethics`, `slides`, `protocol`, `results`. It is assumed that these documents will be written in LaTeX. However, templates are currently not provided.
 
data
--
This is where you will store all of your data. Raw data should be accessible, but never modified. Thus, all raw data should be kept in the `raw_data` folder. Subfolders can be added to suit the project.  

You will subsequently process and analyse your data by running your programs or commercial software. The data that are generated from these steps should be saved in a separate location, the `proc` folder. 

In theory, the processed data can be re-generated by re-running your code. However, there are situations where decisions are made by the user (e.g., exclude trials, manually selecting the start of events) during the initial processing of the data. These details should be saved because they will be needed if ever the data needs to be reprocessed. As much as possible, your programs should access these 'details' files and use the information they contain to process the data. In this way, someone else will be able to run your code and obtain the same results without requiring user input.

There are some types of data that require lots of manual processing. One example is sorting of spike signals (e.g., neuron recordings) in neurophysiology. While the raw signals are useful, many hours are usually spent running spike sorting algorithms and validating their output. Depending on the complexity of these signals, as much as 20-50% of the sorting is done manually. This manual sorting cannot easily be documented or reproduced in computer code, and the sorted signals and their associated spike-times are often treated as a form of raw data. In this case, an additional folder may be required. 

doc
--
The documents folder is where all the generated documents, such as formatted PDF documents, figures, etc are to be located. For example, when preparing a manuscript, you write the text in a LaTeX file located in the `src` folder, but the formatted manuscript that you want to send to your collaborators or a journal is located in the `doc` folder. 

This style of working may seem a little foreign to some, especially if you are only familiar with WYSIWYG word processors (what you see is what you get). I have yet to figure out the best way to use this template if you primarily use such programs to do your work. The source file and the actual document are the same. You will obviously want to keep a backup of the files in `src` and `doc`. However, if every document is prepared in Word, the likelihood is that you will have several versions of certain documents (e.g., manuscript_draft.doc, manuscript_final.doc, manuscript_final_MH_comments.doc). 

One possibility would be to keep all versions in the `src` folder, but export a PDF of the current version of the document to the `doc` when it is at a certain stage (e.g., final_draft.pdf, submitted_version.pdf). This and other approaches are all likely to be suboptimal because they require many versions of each document to be saved. This is necessary if you want to have a history of the changes made by you or one of your collaborators. In LibreOffice and Word, once a change is accepted, the record of this change disappears (unless you use the version tool in these word processors, but few people know they exist or know how to use them properly). 

At present, I write my notes and manuscripts using LaTeX. I also write computer code to process data and generate figures. However, I prepare ethics forms, testing sheets, protocol details, etc., using LibreOffice; these are kept in the `doc` folder. Eventually I would like to have template folders created in the `src` folder that contain LaTeX skeleton for these files. 
