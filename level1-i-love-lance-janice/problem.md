# **I Love Lance Janice**

## **Description**

You've caught two of your fellow minions passing coded notes back and forth - while they're on duty, no less! Worse, you're pretty sure it's not job-related - they're both huge fans of the space soap opera ""Lance & Janice"". You know how much Commander Lambda hates waste, so if you can prove that these minions are wasting her time passing non-job-related notes, it'll put you that much closer to a promotion. 

Fortunately for you, the minions aren't exactly advanced cryptographers. In their code, every lowercase letter [a..z] is replaced with the corresponding one in [z..a], while every other character (including uppercase letters and punctuation) is left untouched.  That is, 'a' becomes 'z', 'b' becomes 'y', 'c' becomes 'x', etc.  For instance, the word ""vmxibkgrlm"", when decoded, would become ""encryption"".

Write a function called solution(s) which takes in a string and returns the deciphered string so you can show the commander proof that these minions are talking about ""Lance & Janice"" instead of doing their jobs.

## **Languages**

To provide a Python solution, edit solution.py <br>
To provide a Java solution, edit Solution.java

## **Test Cases**

Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

### -- Python cases -- <br>
**Input:** <br>
```bash
solution.solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
```
**Output:**<br>
```bash
did you see last night's episode?
```

**Input:**<br>
```bash
solution.solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
```
**Output:**<br>
```bash
Yeah! I can't believe Lance lost his job at the colony!!
```

### -- Java cases --
**Input:**<br>
```bash
Solution.solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
```
**Output:**<br>
```bash
Yeah! I can't believe Lance lost his job at the colony!!
```

**Input:**<br>
```bash
Solution.solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
```
**Output:**<br>
```bash
did you see last night's episode?
```

## **Constraints**

**Java**

Your code will be compiled using standard Java 8. All tests will be run by calling the solution() method inside the Solution class

Execution time is limited.

Wildcard imports and some specific classes are restricted (e.g. java.lang.ClassLoader). You will receive an error when you verify your solution if you have used a blacklisted class.

Third-party libraries, input/output operations, spawning threads or processes and changes to the execution environment are not allowed.

Your solution must be under 32000 characters in length including new lines and and other non-printing characters.

**Python**

Your code will run inside a Python 2.7.13 sandbox. All tests will be run by calling the solution() function.

Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.

Input/output operations are not allowed.

Your solution must be under 32000 characters in length including new lines and and other non-printing characters.

