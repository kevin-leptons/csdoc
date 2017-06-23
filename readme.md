# COMPUTER SCIENCE COURSES

Stanford courses in Computer Science.

Kevin Leptons <kevin.leptons@gmail.com> <br>
June, 2017

# FEATURES

- CS106B - Programming Abstractions
- CS107 - Computer Organization and Systems
- CS110 - Principles of Computer Systems
- CS103 - Mathematical Foundations of Computing
- CS109 - Introduction to Probability for Computer Scientists
- CS161 - Data Structure and Algorithms

# USAGE

```bash
# because size of documents is big ~0.5GB, no package will be build
# instead that, an executable file will be link to system
# and you can use csdoc anywhere

# source
git clone https://github.com/kevin-leptons/csdoc.git
cd csdoc

# virtual environemnt
./env init
. venv/bin/active
./env install

# build
./ctl build

# register executable file with system
./env reg

# now you can use csdoc command anywhere
# even without virtual environemnt
csdoc --help

# if you want to remove csdoc, remember unregister
# executable file from system
./env ureg
```

# DEVELOPMENT

```bash
# do same thing as usage steps
# then develop by create or edit course in src/course directory

# metadata of course put in src/course/<cid>/index.yaml
# see an early exist course for example

# units of course put in src/course/<cid>/<uid>.pdf
# for example src/course/cs103/001.pdf

# build
./ctl build

# or clear
./ctl build --clear

# test csdoc command
csdoc list
```

# REFERENCES

- [Stanford CS Overview](http://csmajor.stanford.edu/Requirements.shtml)
