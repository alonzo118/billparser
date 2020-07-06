# Bill-Parser

This application creates a CLI tool to search summaries of Senate Resolution Bills stored in zipped XML files using provided regular expressions.
The application is currently running with a provided .zip file for Senate Resolutions Bills in the
116th session or *BILLSTATUS-116-sres.zip*.

```bash
$ python billparser.py -h
usage: billparser.py [SEARCH] [OPTION]...

Finds matches to a given regular expression on Senate Resolutions Bills in the 116th session stored as XML files in a .zip archive

positional arguments:
  search         the regular expression to match on

optional arguments:
  -h, --help     show this help message and exit
  -t, --text     enable the return of the matched summary text with highlighted matches
  -v, --version  show program's version number and exit

```
Example search:

```bash
$ python billparser.py "American \w+ Bureau" -t
Found the following bill(s):
SRES 39: This resolution commemorates the 100th anniversary of the American Farm Bureau Federation and recognizes its efforts to promote and advocate for U.S. farm and ranch interests.
```



# Running Locally
####Note: This application runs on Python 3.6 or greater.
### 1. Installing Python
If your operating system does not provide you with a Python package, you can download an installer from the [Python official website](https://www.python.org/downloads/). Opening a terminal window and typing pthon3 should display the following:

```bash
$ python3
Python 3.8.3 (default, Jul  1 2020, 20:56:41) 
[Clang 10.0.1 (clang-1001.0.46.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
You can exit the interactive prompt by typing exit() and hitting enter.

### 2. Search
Navigate to the directory this application is located in and begin searching. The CLI will accept a string with any valid regular expression.

```bash
$ python billparser.py "resolution"
Found the following bill(s):
SRES 1
SRES 2
SRES 3
SRES 4
SRES 5
SRES 6
SRES 7
SRES 8
SRES 9
SRES 10
...
```

The -t or --text option will return the summary text that contained a match to the provided regular expression as well as the actual matched text in **Bold**.

```bash
$ python billparser.py "resolution" -t
Found the following bill(s):
SRES 1: This resolution provides for appointment of a Senate committee joined with a House of Representatives committee to notify the President that a quorum of each chamber has assembled.
SRES 2: This resolution informs the House of Representatives that a quorum of the Senate is assembled.
SRES 3: This resolution elects Senator Chuck Grassley from Iowa as the President pro tempore of the Senate.
SRES 4: This resolution notifies the President of the United States of the election of the Honorable Chuck Grassley as President pro tempore of the Senate.
...
```

If no match is found:
```bash
$ python billparser.py "American Revolution" -t
Did not find any bills
```