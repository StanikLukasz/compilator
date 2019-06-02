
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftIFleftELSEnonassoc=ADDASSIGNSUBASSIGNMULASSIGNDIVASSIGNnonassoc<>EQNEQLEQGEQleftPLUSMINUSDOTADDDOTSUBleft*/DOTMULDOTDIVnonassoc\'\' ( ) * , / : ; < = > ADDASSIGN BREAK CONTINUE DIVASSIGN DOTADD DOTDIV DOTMUL DOTSUB ELSE EQ EYE FOR GEQ ID IF INTNUM LEQ MINUS MULASSIGN NEQ ONES PLUS PRINT REALNUM RETURN STRING SUBASSIGN WHILE ZEROS [ ] { }program : instruction_lines\n               | emptyempty : instruction_lines : instruction_lines instruction_line\n                         | instruction_lineinstruction_line : if_else\n                        | while_loop\n                        | for_loop\n                        | code_block\n                        | instruction \';\'if_else : IF condition instruction_line\n               | IF condition instruction_line ELSE instruction_linewhile_loop : WHILE condition instruction_linefor_loop : FOR identifier \'=\' range instruction_linecode_block : \'{\' program \'}\' condition : \'(\' bool_expression \')\'bool_expression : expression comparison_op expressioncomparison_op : \'<\'\n                     | \'>\'\n                     | EQ\n                     | NEQ\n                     | GEQ\n                     | LEQrange : id_or_number \':\' id_or_numberinstruction : assignment\n                   | printing\n                   | continue_statement\n                   | break_statement\n                   | returningassignment : identifier assignment_op expressionprinting : PRINT array_linecontinue_statement : CONTINUEbreak_statement : BREAKreturning : RETURN expressionassignment_op : \'=\'\n                     | ADDASSIGN\n                     | SUBASSIGN\n                     | MULASSIGN\n                     | DIVASSIGNexpression : expression_binary\n                  | array\n                  | array_special\n                  | transposition\n                  | negation\n                  | expression_group\n                  | elementaryarray : \'[\' array_lines \']\' array_lines : array_lines \';\' array_line\n                   | array_linearray_line : array_line \',\' expression\n                  | expressionarray_special : ZEROS array_special_specifier\n                     | ONES array_special_specifier\n                     | EYE array_special_specifier array_special_specifier : \'(\' id_or_number \')\'transposition : identifier "\'"\n                     | array "\'" negation : MINUS expressionexpression_binary : normal_binary_expression\n                         | dot_binary_expressionnormal_binary_expression : add_expression\n                                | sub_expression\n                                | mul_expression\n                                | div_expressiondot_binary_expression : dot_add_expression\n                             | dot_sub_expression\n                             | dot_mul_expression\n                             | dot_div_expressionadd_expression : expression PLUS expressionsub_expression : expression MINUS expressionmul_expression : expression \'*\' expressiondiv_expression : expression \'/\' expressiondot_add_expression : expression DOTADD expressiondot_sub_expression : expression DOTSUB expressiondot_mul_expression : expression DOTMUL expressiondot_div_expression : expression DOTDIV expressionexpression_group : \'(\' expression \')\' elementary : id_or_number\n                  | texttext : STRINGid_or_number : identifier\n                    | numberidentifier : ID \'[\' array_line \']\'\n                  | IDnumber : integer\n              | realinteger : INTNUMreal : REALNUM'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,7,8,25,26,74,77,80,127,129,],[-3,0,-1,-2,-5,-6,-7,-8,-9,-4,-10,-11,-13,-15,-12,-14,]),'IF':([0,2,4,5,6,7,8,14,24,25,26,27,29,66,68,69,70,71,74,77,80,101,102,110,111,126,127,129,133,],[10,10,-5,-6,-7,-8,-9,10,-84,-4,-10,10,10,-82,-85,-86,-87,-88,-11,-13,-15,10,-16,-81,10,-83,-12,-14,-24,]),'WHILE':([0,2,4,5,6,7,8,14,24,25,26,27,29,66,68,69,70,71,74,77,80,101,102,110,111,126,127,129,133,],[11,11,-5,-6,-7,-8,-9,11,-84,-4,-10,11,11,-82,-85,-86,-87,-88,-11,-13,-15,11,-16,-81,11,-83,-12,-14,-24,]),'FOR':([0,2,4,5,6,7,8,14,24,25,26,27,29,66,68,69,70,71,74,77,80,101,102,110,111,126,127,129,133,],[12,12,-5,-6,-7,-8,-9,12,-84,-4,-10,12,12,-82,-85,-86,-87,-88,-11,-13,-15,12,-16,-81,12,-83,-12,-14,-24,]),'{':([0,2,4,5,6,7,8,14,24,25,26,27,29,66,68,69,70,71,74,77,80,101,102,110,111,126,127,129,133,],[14,14,-5,-6,-7,-8,-9,14,-84,-4,-10,14,14,-82,-85,-86,-87,-88,-11,-13,-15,14,-16,-81,14,-83,-12,-14,-24,]),'PRINT':([0,2,4,5,6,7,8,14,24,25,26,27,29,66,68,69,70,71,74,77,80,101,102,110,111,126,127,129,133,],[20,20,-5,-6,-7,-8,-9,20,-84,-4,-10,20,20,-82,-85,-86,-87,-88,-11,-13,-15,20,-16,-81,20,-83,-12,-14,-24,]),'CONTINUE':([0,2,4,5,6,7,8,14,24,25,26,27,29,66,68,69,70,71,74,77,80,101,102,110,111,126,127,129,133,],[21,21,-5,-6,-7,-8,-9,21,-84,-4,-10,21,21,-82,-85,-86,-87,-88,-11,-13,-15,21,-16,-81,21,-83,-12,-14,-24,]),'BREAK':([0,2,4,5,6,7,8,14,24,25,26,27,29,66,68,69,70,71,74,77,80,101,102,110,111,126,127,129,133,],[22,22,-5,-6,-7,-8,-9,22,-84,-4,-10,22,22,-82,-85,-86,-87,-88,-11,-13,-15,22,-16,-81,22,-83,-12,-14,-24,]),'RETURN':([0,2,4,5,6,7,8,14,24,25,26,27,29,66,68,69,70,71,74,77,80,101,102,110,111,126,127,129,133,],[23,23,-5,-6,-7,-8,-9,23,-84,-4,-10,23,23,-82,-85,-86,-87,-88,-11,-13,-15,23,-16,-81,23,-83,-12,-14,-24,]),'ID':([0,2,4,5,6,7,8,12,14,20,23,24,25,26,27,28,29,31,32,33,34,35,36,49,54,55,66,68,69,70,71,73,74,77,78,80,81,82,83,84,85,86,87,88,89,94,101,102,103,104,105,106,107,108,109,110,111,123,126,127,129,130,133,],[24,24,-5,-6,-7,-8,-9,24,24,24,24,-84,-4,-10,24,24,24,24,-35,-36,-37,-38,-39,24,24,24,-82,-85,-86,-87,-88,24,-11,-13,24,-15,24,24,24,24,24,24,24,24,24,24,24,-16,24,-18,-19,-20,-21,-22,-23,-81,24,24,-83,-12,-14,24,-24,]),'}':([2,3,4,5,6,7,8,14,25,26,37,74,77,80,127,129,],[-1,-2,-5,-6,-7,-8,-9,-3,-4,-10,80,-11,-13,-15,-12,-14,]),'ELSE':([5,6,7,8,26,74,77,80,127,129,],[-6,-7,-8,-9,-10,101,-13,-15,-12,-14,]),';':([9,15,16,17,18,19,21,22,24,38,39,40,41,42,43,44,45,46,47,48,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,79,90,91,92,93,95,96,97,98,113,114,115,116,117,118,119,120,121,122,125,126,131,132,],[26,-25,-26,-27,-28,-29,-32,-33,-84,-31,-51,-40,-41,-42,-43,-44,-45,-46,-59,-60,-81,-78,-79,-61,-62,-63,-64,-65,-66,-67,-68,-82,-80,-85,-86,-87,-88,-34,-30,-57,123,-49,-52,-53,-54,-56,-58,-50,-69,-70,-71,-72,-73,-74,-75,-76,-47,-77,-83,-48,-55,]),'(':([10,11,20,23,28,31,32,33,34,35,36,49,50,51,52,54,55,73,81,82,83,84,85,86,87,88,89,103,104,105,106,107,108,109,123,],[28,28,55,55,55,55,-35,-36,-37,-38,-39,55,94,94,94,55,55,55,55,55,55,55,55,55,55,55,55,55,-18,-19,-20,-21,-22,-23,55,]),'=':([13,24,30,126,],[32,-84,78,-83,]),'ADDASSIGN':([13,24,126,],[33,-84,-83,]),'SUBASSIGN':([13,24,126,],[34,-84,-83,]),'MULASSIGN':([13,24,126,],[35,-84,-83,]),'DIVASSIGN':([13,24,126,],[36,-84,-83,]),'[':([20,23,24,28,31,32,33,34,35,36,49,54,55,73,81,82,83,84,85,86,87,88,89,103,104,105,106,107,108,109,123,],[49,49,73,49,49,-35,-36,-37,-38,-39,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-18,-19,-20,-21,-22,-23,49,]),'ZEROS':([20,23,28,31,32,33,34,35,36,49,54,55,73,81,82,83,84,85,86,87,88,89,103,104,105,106,107,108,109,123,],[50,50,50,50,-35,-36,-37,-38,-39,50,50,50,50,50,50,50,50,50,50,50,50,50,50,-18,-19,-20,-21,-22,-23,50,]),'ONES':([20,23,28,31,32,33,34,35,36,49,54,55,73,81,82,83,84,85,86,87,88,89,103,104,105,106,107,108,109,123,],[51,51,51,51,-35,-36,-37,-38,-39,51,51,51,51,51,51,51,51,51,51,51,51,51,51,-18,-19,-20,-21,-22,-23,51,]),'EYE':([20,23,28,31,32,33,34,35,36,49,54,55,73,81,82,83,84,85,86,87,88,89,103,104,105,106,107,108,109,123,],[52,52,52,52,-35,-36,-37,-38,-39,52,52,52,52,52,52,52,52,52,52,52,52,52,52,-18,-19,-20,-21,-22,-23,52,]),'MINUS':([20,23,24,28,31,32,33,34,35,36,39,40,41,42,43,44,45,46,47,48,49,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,76,79,81,82,83,84,85,86,87,88,89,90,93,95,96,97,98,99,103,104,105,106,107,108,109,113,114,115,116,117,118,119,120,121,122,123,125,126,128,132,],[54,54,-84,54,54,-35,-36,-37,-38,-39,83,-40,-41,-42,-43,-44,-45,-46,-59,-60,54,-81,54,54,-78,-79,-61,-62,-63,-64,-65,-66,-67,-68,-82,-80,-85,-86,-87,-88,83,54,83,83,54,54,54,54,54,54,54,54,54,-57,-52,-53,-54,-56,-58,83,54,-18,-19,-20,-21,-22,-23,83,-69,-70,-71,-72,-73,-74,-75,-76,-47,54,-77,-83,83,-55,]),'STRING':([20,23,28,31,32,33,34,35,36,49,54,55,73,81,82,83,84,85,86,87,88,89,103,104,105,106,107,108,109,123,],[67,67,67,67,-35,-36,-37,-38,-39,67,67,67,67,67,67,67,67,67,67,67,67,67,67,-18,-19,-20,-21,-22,-23,67,]),'INTNUM':([20,23,28,31,32,33,34,35,36,49,54,55,73,78,81,82,83,84,85,86,87,88,89,94,103,104,105,106,107,108,109,123,130,],[70,70,70,70,-35,-36,-37,-38,-39,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,-18,-19,-20,-21,-22,-23,70,70,]),'REALNUM':([20,23,28,31,32,33,34,35,36,49,54,55,73,78,81,82,83,84,85,86,87,88,89,94,103,104,105,106,107,108,109,123,130,],[71,71,71,71,-35,-36,-37,-38,-39,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,-18,-19,-20,-21,-22,-23,71,71,]),"'":([24,41,53,122,126,],[-84,90,97,-47,-83,]),'PLUS':([24,39,40,41,42,43,44,45,46,47,48,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,79,90,93,95,96,97,98,99,113,114,115,116,117,118,119,120,121,122,125,126,128,132,],[-84,82,-40,-41,-42,-43,-44,-45,-46,-59,-60,-81,-78,-79,-61,-62,-63,-64,-65,-66,-67,-68,-82,-80,-85,-86,-87,-88,82,82,82,-57,-52,-53,-54,-56,-58,82,82,-69,-70,-71,-72,-73,-74,-75,-76,-47,-77,-83,82,-55,]),'*':([24,39,40,41,42,43,44,45,46,47,48,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,79,90,93,95,96,97,98,99,113,114,115,116,117,118,119,120,121,122,125,126,128,132,],[-84,84,-40,-41,-42,-43,-44,-45,-46,-59,-60,-81,-78,-79,-61,-62,-63,-64,-65,-66,-67,-68,-82,-80,-85,-86,-87,-88,84,84,84,-57,-52,-53,-54,-56,84,84,84,84,84,-71,-72,84,84,-75,-76,-47,-77,-83,84,-55,]),'/':([24,39,40,41,42,43,44,45,46,47,48,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,79,90,93,95,96,97,98,99,113,114,115,116,117,118,119,120,121,122,125,126,128,132,],[-84,85,-40,-41,-42,-43,-44,-45,-46,-59,-60,-81,-78,-79,-61,-62,-63,-64,-65,-66,-67,-68,-82,-80,-85,-86,-87,-88,85,85,85,-57,-52,-53,-54,-56,85,85,85,85,85,-71,-72,85,85,-75,-76,-47,-77,-83,85,-55,]),'DOTADD':([24,39,40,41,42,43,44,45,46,47,48,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,79,90,93,95,96,97,98,99,113,114,115,116,117,118,119,120,121,122,125,126,128,132,],[-84,86,-40,-41,-42,-43,-44,-45,-46,-59,-60,-81,-78,-79,-61,-62,-63,-64,-65,-66,-67,-68,-82,-80,-85,-86,-87,-88,86,86,86,-57,-52,-53,-54,-56,-58,86,86,-69,-70,-71,-72,-73,-74,-75,-76,-47,-77,-83,86,-55,]),'DOTSUB':([24,39,40,41,42,43,44,45,46,47,48,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,79,90,93,95,96,97,98,99,113,114,115,116,117,118,119,120,121,122,125,126,128,132,],[-84,87,-40,-41,-42,-43,-44,-45,-46,-59,-60,-81,-78,-79,-61,-62,-63,-64,-65,-66,-67,-68,-82,-80,-85,-86,-87,-88,87,87,87,-57,-52,-53,-54,-56,-58,87,87,-69,-70,-71,-72,-73,-74,-75,-76,-47,-77,-83,87,-55,]),'DOTMUL':([24,39,40,41,42,43,44,45,46,47,48,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,79,90,93,95,96,97,98,99,113,114,115,116,117,118,119,120,121,122,125,126,128,132,],[-84,88,-40,-41,-42,-43,-44,-45,-46,-59,-60,-81,-78,-79,-61,-62,-63,-64,-65,-66,-67,-68,-82,-80,-85,-86,-87,-88,88,88,88,-57,-52,-53,-54,-56,88,88,88,88,88,-71,-72,88,88,-75,-76,-47,-77,-83,88,-55,]),'DOTDIV':([24,39,40,41,42,43,44,45,46,47,48,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,76,79,90,93,95,96,97,98,99,113,114,115,116,117,118,119,120,121,122,125,126,128,132,],[-84,89,-40,-41,-42,-43,-44,-45,-46,-59,-60,-81,-78,-79,-61,-62,-63,-64,-65,-66,-67,-68,-82,-80,-85,-86,-87,-88,89,89,89,-57,-52,-53,-54,-56,89,89,89,89,89,-71,-72,89,89,-75,-76,-47,-77,-83,89,-55,]),',':([24,38,39,40,41,42,43,44,45,46,47,48,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,90,92,93,95,96,97,98,100,113,114,115,116,117,118,119,120,121,122,125,126,131,132,],[-84,81,-51,-40,-41,-42,-43,-44,-45,-46,-59,-60,-81,-78,-79,-61,-62,-63,-64,-65,-66,-67,-68,-82,-80,-85,-86,-87,-88,-57,81,-52,-53,-54,-56,-58,81,-50,-69,-70,-71,-72,-73,-74,-75,-76,-47,-77,-83,81,-55,]),'<':([24,40,41,42,43,44,45,46,47,48,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,76,90,93,95,96,97,98,114,115,116,117,118,119,120,121,122,125,126,132,],[-84,-40,-41,-42,-43,-44,-45,-46,-59,-60,-81,-78,-79,-61,-62,-63,-64,-65,-66,-67,-68,-82,-80,-85,-86,-87,-88,104,-57,-52,-53,-54,-56,-58,-69,-70,-71,-72,-73,-74,-75,-76,-47,-77,-83,-55,]),'>':([24,40,41,42,43,44,45,46,47,48,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,76,90,93,95,96,97,98,114,115,116,117,118,119,120,121,122,125,126,132,],[-84,-40,-41,-42,-43,-44,-45,-46,-59,-60,-81,-78,-79,-61,-62,-63,-64,-65,-66,-67,-68,-82,-80,-85,-86,-87,-88,105,-57,-52,-53,-54,-56,-58,-69,-70,-71,-72,-73,-74,-75,-76,-47,-77,-83,-55,]),'EQ':([24,40,41,42,43,44,45,46,47,48,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,76,90,93,95,96,97,98,114,115,116,117,118,119,120,121,122,125,126,132,],[-84,-40,-41,-42,-43,-44,-45,-46,-59,-60,-81,-78,-79,-61,-62,-63,-64,-65,-66,-67,-68,-82,-80,-85,-86,-87,-88,106,-57,-52,-53,-54,-56,-58,-69,-70,-71,-72,-73,-74,-75,-76,-47,-77,-83,-55,]),'NEQ':([24,40,41,42,43,44,45,46,47,48,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,76,90,93,95,96,97,98,114,115,116,117,118,119,120,121,122,125,126,132,],[-84,-40,-41,-42,-43,-44,-45,-46,-59,-60,-81,-78,-79,-61,-62,-63,-64,-65,-66,-67,-68,-82,-80,-85,-86,-87,-88,107,-57,-52,-53,-54,-56,-58,-69,-70,-71,-72,-73,-74,-75,-76,-47,-77,-83,-55,]),'GEQ':([24,40,41,42,43,44,45,46,47,48,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,76,90,93,95,96,97,98,114,115,116,117,118,119,120,121,122,125,126,132,],[-84,-40,-41,-42,-43,-44,-45,-46,-59,-60,-81,-78,-79,-61,-62,-63,-64,-65,-66,-67,-68,-82,-80,-85,-86,-87,-88,108,-57,-52,-53,-54,-56,-58,-69,-70,-71,-72,-73,-74,-75,-76,-47,-77,-83,-55,]),'LEQ':([24,40,41,42,43,44,45,46,47,48,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,76,90,93,95,96,97,98,114,115,116,117,118,119,120,121,122,125,126,132,],[-84,-40,-41,-42,-43,-44,-45,-46,-59,-60,-81,-78,-79,-61,-62,-63,-64,-65,-66,-67,-68,-82,-80,-85,-86,-87,-88,109,-57,-52,-53,-54,-56,-58,-69,-70,-71,-72,-73,-74,-75,-76,-47,-77,-83,-55,]),']':([24,39,40,41,42,43,44,45,46,47,48,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,90,91,92,93,95,96,97,98,100,113,114,115,116,117,118,119,120,121,122,125,126,131,132,],[-84,-51,-40,-41,-42,-43,-44,-45,-46,-59,-60,-81,-78,-79,-61,-62,-63,-64,-65,-66,-67,-68,-82,-80,-85,-86,-87,-88,-57,122,-49,-52,-53,-54,-56,-58,126,-50,-69,-70,-71,-72,-73,-74,-75,-76,-47,-77,-83,-48,-55,]),')':([24,40,41,42,43,44,45,46,47,48,53,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,75,90,93,95,96,97,98,99,110,114,115,116,117,118,119,120,121,122,124,125,126,128,132,],[-84,-40,-41,-42,-43,-44,-45,-46,-59,-60,-81,-78,-79,-61,-62,-63,-64,-65,-66,-67,-68,-82,-80,-85,-86,-87,-88,102,-57,-52,-53,-54,-56,-58,125,-81,-69,-70,-71,-72,-73,-74,-75,-76,-47,132,-77,-83,-17,-55,]),':':([24,66,68,69,70,71,110,112,126,],[-84,-82,-85,-86,-87,-88,-81,130,-83,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,14,],[1,37,]),'instruction_lines':([0,14,],[2,2,]),'empty':([0,14,],[3,3,]),'instruction_line':([0,2,14,27,29,101,111,],[4,25,4,74,77,127,129,]),'if_else':([0,2,14,27,29,101,111,],[5,5,5,5,5,5,5,]),'while_loop':([0,2,14,27,29,101,111,],[6,6,6,6,6,6,6,]),'for_loop':([0,2,14,27,29,101,111,],[7,7,7,7,7,7,7,]),'code_block':([0,2,14,27,29,101,111,],[8,8,8,8,8,8,8,]),'instruction':([0,2,14,27,29,101,111,],[9,9,9,9,9,9,9,]),'identifier':([0,2,12,14,20,23,27,28,29,31,49,54,55,73,78,81,82,83,84,85,86,87,88,89,94,101,103,111,123,130,],[13,13,30,13,53,53,13,53,13,53,53,53,53,53,110,53,53,53,53,53,53,53,53,53,110,13,53,13,53,110,]),'assignment':([0,2,14,27,29,101,111,],[15,15,15,15,15,15,15,]),'printing':([0,2,14,27,29,101,111,],[16,16,16,16,16,16,16,]),'continue_statement':([0,2,14,27,29,101,111,],[17,17,17,17,17,17,17,]),'break_statement':([0,2,14,27,29,101,111,],[18,18,18,18,18,18,18,]),'returning':([0,2,14,27,29,101,111,],[19,19,19,19,19,19,19,]),'condition':([10,11,],[27,29,]),'assignment_op':([13,],[31,]),'array_line':([20,49,73,123,],[38,92,100,131,]),'expression':([20,23,28,31,49,54,55,73,81,82,83,84,85,86,87,88,89,103,123,],[39,72,76,79,39,98,99,39,113,114,115,116,117,118,119,120,121,128,39,]),'expression_binary':([20,23,28,31,49,54,55,73,81,82,83,84,85,86,87,88,89,103,123,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'array':([20,23,28,31,49,54,55,73,81,82,83,84,85,86,87,88,89,103,123,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'array_special':([20,23,28,31,49,54,55,73,81,82,83,84,85,86,87,88,89,103,123,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'transposition':([20,23,28,31,49,54,55,73,81,82,83,84,85,86,87,88,89,103,123,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'negation':([20,23,28,31,49,54,55,73,81,82,83,84,85,86,87,88,89,103,123,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'expression_group':([20,23,28,31,49,54,55,73,81,82,83,84,85,86,87,88,89,103,123,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'elementary':([20,23,28,31,49,54,55,73,81,82,83,84,85,86,87,88,89,103,123,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'normal_binary_expression':([20,23,28,31,49,54,55,73,81,82,83,84,85,86,87,88,89,103,123,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'dot_binary_expression':([20,23,28,31,49,54,55,73,81,82,83,84,85,86,87,88,89,103,123,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'id_or_number':([20,23,28,31,49,54,55,73,78,81,82,83,84,85,86,87,88,89,94,103,123,130,],[56,56,56,56,56,56,56,56,112,56,56,56,56,56,56,56,56,56,124,56,56,133,]),'text':([20,23,28,31,49,54,55,73,81,82,83,84,85,86,87,88,89,103,123,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'add_expression':([20,23,28,31,49,54,55,73,81,82,83,84,85,86,87,88,89,103,123,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'sub_expression':([20,23,28,31,49,54,55,73,81,82,83,84,85,86,87,88,89,103,123,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'mul_expression':([20,23,28,31,49,54,55,73,81,82,83,84,85,86,87,88,89,103,123,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'div_expression':([20,23,28,31,49,54,55,73,81,82,83,84,85,86,87,88,89,103,123,],[61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,]),'dot_add_expression':([20,23,28,31,49,54,55,73,81,82,83,84,85,86,87,88,89,103,123,],[62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'dot_sub_expression':([20,23,28,31,49,54,55,73,81,82,83,84,85,86,87,88,89,103,123,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'dot_mul_expression':([20,23,28,31,49,54,55,73,81,82,83,84,85,86,87,88,89,103,123,],[64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'dot_div_expression':([20,23,28,31,49,54,55,73,81,82,83,84,85,86,87,88,89,103,123,],[65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,]),'number':([20,23,28,31,49,54,55,73,78,81,82,83,84,85,86,87,88,89,94,103,123,130,],[66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'integer':([20,23,28,31,49,54,55,73,78,81,82,83,84,85,86,87,88,89,94,103,123,130,],[68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,]),'real':([20,23,28,31,49,54,55,73,78,81,82,83,84,85,86,87,88,89,94,103,123,130,],[69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,]),'bool_expression':([28,],[75,]),'array_lines':([49,],[91,]),'array_special_specifier':([50,51,52,],[93,95,96,]),'comparison_op':([76,],[103,]),'range':([78,],[111,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> instruction_lines','program',1,'p_program','parser.py',55),
  ('program -> empty','program',1,'p_program','parser.py',56),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',60),
  ('instruction_lines -> instruction_lines instruction_line','instruction_lines',2,'p_instructions','parser.py',64),
  ('instruction_lines -> instruction_line','instruction_lines',1,'p_instructions','parser.py',65),
  ('instruction_line -> if_else','instruction_line',1,'p_instruction_line','parser.py',74),
  ('instruction_line -> while_loop','instruction_line',1,'p_instruction_line','parser.py',75),
  ('instruction_line -> for_loop','instruction_line',1,'p_instruction_line','parser.py',76),
  ('instruction_line -> code_block','instruction_line',1,'p_instruction_line','parser.py',77),
  ('instruction_line -> instruction ;','instruction_line',2,'p_instruction_line','parser.py',78),
  ('if_else -> IF condition instruction_line','if_else',3,'p_if_else','parser.py',82),
  ('if_else -> IF condition instruction_line ELSE instruction_line','if_else',5,'p_if_else','parser.py',83),
  ('while_loop -> WHILE condition instruction_line','while_loop',3,'p_while_loop','parser.py',90),
  ('for_loop -> FOR identifier = range instruction_line','for_loop',5,'p_for_loop','parser.py',94),
  ('code_block -> { program }','code_block',3,'p_code_block','parser.py',98),
  ('condition -> ( bool_expression )','condition',3,'p_condition','parser.py',103),
  ('bool_expression -> expression comparison_op expression','bool_expression',3,'p_bool_expression','parser.py',107),
  ('comparison_op -> <','comparison_op',1,'p_comparison_op','parser.py',111),
  ('comparison_op -> >','comparison_op',1,'p_comparison_op','parser.py',112),
  ('comparison_op -> EQ','comparison_op',1,'p_comparison_op','parser.py',113),
  ('comparison_op -> NEQ','comparison_op',1,'p_comparison_op','parser.py',114),
  ('comparison_op -> GEQ','comparison_op',1,'p_comparison_op','parser.py',115),
  ('comparison_op -> LEQ','comparison_op',1,'p_comparison_op','parser.py',116),
  ('range -> id_or_number : id_or_number','range',3,'p_range','parser.py',121),
  ('instruction -> assignment','instruction',1,'p_instruction','parser.py',128),
  ('instruction -> printing','instruction',1,'p_instruction','parser.py',129),
  ('instruction -> continue_statement','instruction',1,'p_instruction','parser.py',130),
  ('instruction -> break_statement','instruction',1,'p_instruction','parser.py',131),
  ('instruction -> returning','instruction',1,'p_instruction','parser.py',132),
  ('assignment -> identifier assignment_op expression','assignment',3,'p_assignment','parser.py',136),
  ('printing -> PRINT array_line','printing',2,'p_printing','parser.py',140),
  ('continue_statement -> CONTINUE','continue_statement',1,'p_continue_statement','parser.py',144),
  ('break_statement -> BREAK','break_statement',1,'p_break_statement','parser.py',148),
  ('returning -> RETURN expression','returning',2,'p_returning','parser.py',152),
  ('assignment_op -> =','assignment_op',1,'p_assignment_op','parser.py',157),
  ('assignment_op -> ADDASSIGN','assignment_op',1,'p_assignment_op','parser.py',158),
  ('assignment_op -> SUBASSIGN','assignment_op',1,'p_assignment_op','parser.py',159),
  ('assignment_op -> MULASSIGN','assignment_op',1,'p_assignment_op','parser.py',160),
  ('assignment_op -> DIVASSIGN','assignment_op',1,'p_assignment_op','parser.py',161),
  ('expression -> expression_binary','expression',1,'p_expression','parser.py',168),
  ('expression -> array','expression',1,'p_expression','parser.py',169),
  ('expression -> array_special','expression',1,'p_expression','parser.py',170),
  ('expression -> transposition','expression',1,'p_expression','parser.py',171),
  ('expression -> negation','expression',1,'p_expression','parser.py',172),
  ('expression -> expression_group','expression',1,'p_expression','parser.py',173),
  ('expression -> elementary','expression',1,'p_expression','parser.py',174),
  ('array -> [ array_lines ]','array',3,'p_array','parser.py',180),
  ('array_lines -> array_lines ; array_line','array_lines',3,'p_array_lines','parser.py',184),
  ('array_lines -> array_line','array_lines',1,'p_array_lines','parser.py',185),
  ('array_line -> array_line , expression','array_line',3,'p_array_line','parser.py',192),
  ('array_line -> expression','array_line',1,'p_array_line','parser.py',193),
  ('array_special -> ZEROS array_special_specifier','array_special',2,'p_array_special','parser.py',201),
  ('array_special -> ONES array_special_specifier','array_special',2,'p_array_special','parser.py',202),
  ('array_special -> EYE array_special_specifier','array_special',2,'p_array_special','parser.py',203),
  ('array_special_specifier -> ( id_or_number )','array_special_specifier',3,'p_array_special_specifier','parser.py',207),
  ("transposition -> identifier '",'transposition',2,'p_transposition','parser.py',212),
  ("transposition -> array '",'transposition',2,'p_transposition','parser.py',213),
  ('negation -> MINUS expression','negation',2,'p_negation','parser.py',218),
  ('expression_binary -> normal_binary_expression','expression_binary',1,'p_expression_binary','parser.py',223),
  ('expression_binary -> dot_binary_expression','expression_binary',1,'p_expression_binary','parser.py',224),
  ('normal_binary_expression -> add_expression','normal_binary_expression',1,'p_normal_binary_expression','parser.py',228),
  ('normal_binary_expression -> sub_expression','normal_binary_expression',1,'p_normal_binary_expression','parser.py',229),
  ('normal_binary_expression -> mul_expression','normal_binary_expression',1,'p_normal_binary_expression','parser.py',230),
  ('normal_binary_expression -> div_expression','normal_binary_expression',1,'p_normal_binary_expression','parser.py',231),
  ('dot_binary_expression -> dot_add_expression','dot_binary_expression',1,'p_dot_binary_expression','parser.py',235),
  ('dot_binary_expression -> dot_sub_expression','dot_binary_expression',1,'p_dot_binary_expression','parser.py',236),
  ('dot_binary_expression -> dot_mul_expression','dot_binary_expression',1,'p_dot_binary_expression','parser.py',237),
  ('dot_binary_expression -> dot_div_expression','dot_binary_expression',1,'p_dot_binary_expression','parser.py',238),
  ('add_expression -> expression PLUS expression','add_expression',3,'p_add_expression','parser.py',242),
  ('sub_expression -> expression MINUS expression','sub_expression',3,'p_sub_expression','parser.py',246),
  ('mul_expression -> expression * expression','mul_expression',3,'p_mul_expression','parser.py',250),
  ('div_expression -> expression / expression','div_expression',3,'p_div_expression','parser.py',254),
  ('dot_add_expression -> expression DOTADD expression','dot_add_expression',3,'p_dot_add_expression','parser.py',258),
  ('dot_sub_expression -> expression DOTSUB expression','dot_sub_expression',3,'p_dot_sub_expression','parser.py',262),
  ('dot_mul_expression -> expression DOTMUL expression','dot_mul_expression',3,'p_dot_mul_expression','parser.py',266),
  ('dot_div_expression -> expression DOTDIV expression','dot_div_expression',3,'p_dot_div_expression','parser.py',270),
  ('expression_group -> ( expression )','expression_group',3,'p_expression_group','parser.py',275),
  ('elementary -> id_or_number','elementary',1,'p_elementary','parser.py',280),
  ('elementary -> text','elementary',1,'p_elementary','parser.py',281),
  ('text -> STRING','text',1,'p_text','parser.py',285),
  ('id_or_number -> identifier','id_or_number',1,'p_id_or_number','parser.py',289),
  ('id_or_number -> number','id_or_number',1,'p_id_or_number','parser.py',290),
  ('identifier -> ID [ array_line ]','identifier',4,'p_identifier','parser.py',294),
  ('identifier -> ID','identifier',1,'p_identifier','parser.py',295),
  ('number -> integer','number',1,'p_number','parser.py',302),
  ('number -> real','number',1,'p_number','parser.py',303),
  ('integer -> INTNUM','integer',1,'p_integer','parser.py',307),
  ('real -> REALNUM','real',1,'p_real','parser.py',311),
]
