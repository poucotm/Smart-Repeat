# Smart Repeat for Sublime Text

Smart Repeat helps to repeat code with incremental/decremental numbers.

* **Usage**
	- Select code to be repeated, it may include Python's format symbol like {...}
	- Run `Smart Repeat : Repeat Code with Numbers` command (default key map : `alt+insert`)
	- Type a range in the input panel as the following : [from]~[to],[↓step],[→step]  
	  ``(e.g. 0~10 or 0~10,2 or 10~0,-1 or 0~5,1,1 ...)``
	- [↓step] means row step, default is 1, [→step] means column step, default is 0
	- The codes will be repeated with incremental or decremental numbers
	- Python's format symbol supports variable formats : binary, hex, leading zeros, ...
	- To use '{' as is, you should type twice as '{{'
	- Refer to Python's format symbol here, [https://www.python.org/dev/peps/pep-3101/](https://www.python.org/dev/peps/pep-3101/)
	- For **sublime text 2 (python 2.x)**, you should insert index behind of ':' in curly brackets like `foo {0:5b} bar {1:3d}`

```java
	e.g)
		abc[{:2d}] = {:2d} + {:2d} + {:2d} + {:2d};

		--> Select and Type Range as 0~10,1,2

		abc[{:2d}] = {:2d} + {:2d} + {:2d} + {:2d};
		abc[ 0] =  2 +  4 +  6 +  8;
		abc[ 1] =  3 +  5 +  7 +  9;
		abc[ 2] =  4 +  6 +  8 + 10;
		abc[ 3] =  5 +  7 +  9 + 11;
		abc[ 4] =  6 +  8 + 10 + 12;
		abc[ 5] =  7 +  9 + 11 + 13;
		abc[ 6] =  8 + 10 + 12 + 14;
		abc[ 7] =  9 + 11 + 13 + 15;
		abc[ 8] = 10 + 12 + 14 + 16;
		abc[ 9] = 11 + 13 + 15 + 17;
		abc[10] = 12 + 14 + 16 + 18;
```

## issues

When you have an issue, tell me through [https://github.com/poucotm/Smart-Repeat/issues](https://github.com/poucotm/Smart-Repeat/issues), or send me an e-mail poucotm@gmail.com, yongchan.jeon@samsung.com