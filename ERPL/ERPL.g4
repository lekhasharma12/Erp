grammar ERPL;

//s : r ;
//r : (a)+ EXIT ;
//a : p | q | m ;
//p : PROCESS WHITESPACE i ;
//q : ROLE WHITESPACE i ;
//m : MAP WHITESPACE ID WHITESPACE TO WHITESPACE ID NEWLINE;
//i : ADD WHITESPACE n ;
//n : ID NEWLINE;

// r : a | EXIT ;
// a : POLICY i | SUBJECT n | PROCESS b | ROLE c | TASK d | MAP ID TO ID ;
// n : LIST | w ;
// w : ADD ID | DELETE ID | MODIFY ID | VIEW ID ;
// i : LIST | o ID ;
// o : ADD | DELETE | MODIFY | VIEW ;
// b : o ID ;
// c : o ID ;
// d : o ID ;r
s : q ;
q : a+ EXIT ;
a : r+ p+ | i+;
r : DEF WS ROLE WS ID NEWLINE ;
p : DEF WS PROCESS WS ID NEWLINE t+ END WS PROCESS NEWLINE;
t : ADD WS (STARTTASK |TASK) WS ID WS ':' WS ID NEWLINE ;
i : RUN WS TASK WS ID NEWLINE;

DEF : 'def' ;
EXIT : 'exit';
ADD : 'add' ;
PROCESS : 'process' ;
ROLE : 'role' ;
TASK : 'task' ;
STARTTASK : 'start task' ;
END : 'end' ;
RUN : 'run' ;
ID : [A-Za-z_]+ ;
WS : (' ' | '\t') ;
NEWLINE : ('\r'? '\n' | '\r')+ ;

//POLICY : 'policy' ;
//TO : 'to' ;
//MAP : 'map' ;
//POSET : 'poset' ;
//SUBJECT : 'subject' ;
//LIST : 'list' ;
//DELETE : 'delete' ;
//VIEW : 'view' ;
//MODIFY : 'modify' ;