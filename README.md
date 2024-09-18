# Introduction 

Web scraping is a technique used to extract data from websites.  It
inolves writing a program to visit multiple web pages to extract
relevant information.

# Scraping a University Website

Let's say you want to gather all the course number and description from the
Capilano University website into one single text file to make it easier to 
look at.  Use this link to start your exploration:  
https://www.capilanou.ca/programs--courses/search--select/find-a-program-or-course/ 


If you look at the page using curl or lynx, you’ll notice the page contains data 
for every course number, with links to the individual course description.  

Create a script that accepts a course code as an argument, and output a text file 
that uses the "tab" key as delimiter (i.e. a tab separated file) with 2 fields: 
"course code" and "course description".

Below is a partial output of this script:

```console
$ ./extract_courses.sh 
Please supply a program code
$ ./extract_courses.sh comp
comp-101        An introduction to the basic concepts underlying computer hardware, software, operating systems, networks, applications, and coding, for students with little or no previous experience. Students also explore some of the social and ethical implications arising from the pervasive use of digital information technologies. The goals of this course are to gain a broad understanding of the science of computing, to develop practical skills applied to the use of the Internet and common computer applications, and to become actively engaged with both the promise and challenges of digital technology.
comp-106        An introduction to the basic concepts of hardware, software, and computer programming using Sparki robots, for students with little or no experience. Students learn to apply fundamental engineering design and programming principles, and are exposed to a variety of topics including robotics and automation, operating systems, and digital communications. The course includes an examination of social issues arising from the application of robotics and automation technologies.
```

Create the `extract_courses.sh` file.

# Hand-in

Once you are satisified with your script, hand in with the following commands:

```
git add -A
git commit -a -m 'submit'
git push
```
