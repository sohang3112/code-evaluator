# code-evaluator
## Final Year Project

Input Args (CLI / interactive):
	- Folders - Code, Test, Input, Output
	- Max Duration (Timeout if this is exceeded)
	- Course Name
	- Extensions (Input, Output, Test)
	
Formats ({..} -> input / known parameter, 
		 <..> -> output / unknown parameter [PARSED])
	- Code   --> {course}.<student>.<extension>          
	- Input  --> test<num>.input
	- Output --> {student}.{num}.output
	- Runtime Error --> {student}.{num}.rte
	- Compile Error --> {student}.{num}.cte
	
	

// { extension : command }
{"c": {"gcc", "-std=c11", "-o", name+".exe", s}}   // s <- filename

Result: 
	Compiled | Not Compiled | Passed all tests | Passed some tests | Did not pass any test


### TODO (Planned)
- Multi Threading