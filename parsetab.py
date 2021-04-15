
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASIGNA ATTRIBUTES CHAR CLASS COLON COMMA CTE_C CTE_F CTE_I DIV DO DOT ELSE EQUALS EXTENDS FLOAT FOR FUNC GT GTE ID IF INT LBRACE LBRACK LETRERO LPAREN LT LTE MAIN METHODS MINUS MULT NEQUALS OR PLUS PROGRAM QUOTE RBRACE RBRACK READ RETURN RPAREN SCOLON THEN TO VAR VOID WHILE WRITE\n    program : PROGRAM ID SCOLON declarClases declarVar definFunc MAIN LPAREN RPAREN LBRACE listaEstatutos RBRACE\n    \n    declarClases : CLASS ID herencia LBRACE ATTRIBUTES declarAttributes METHODS declarMethods RBRACE declarClases\n                 | empty\n    \n    herencia : LT EXTENDS ID GT\n             | empty\n    \n    declarAttributes : listaId COLON tipo SCOLON declarAttributes\n                     | empty\n    \n    listaId : idCall \n            | idCall COMMA listaId\n    \n    idCall : ID\n           | ID LBRACK exp RBRACK\n           | ID LBRACK exp RBRACK LBRACK exp RBRACK\n    \n    tipo : ID\n         | INT\n         | FLOAT\n         | CHAR\n    \n    declarMethods : tipoMethod FUNC ID LPAREN listaParam RPAREN LBRACE listaEstatutos RBRACE declarMethods\n                  | empty\n    \n    tipoMethod : VOID\n               | INT\n               | FLOAT\n               | CHAR\n    \n    listaParam : param\n               | param COMMA listaParam\n               | empty\n    \n    param : idCall COLON tipo\n    \n    declarVar : VAR listaId COLON tipo SCOLON declarVar\n              | empty\n    \n    definFunc : tipoMethod FUNC ID LPAREN listaParam RPAREN declarVar LBRACE listaEstatutos RBRACE definFunc\n              | empty\n    \n    listaEstatutos : estatutos listaEstatutos\n                   | empty\n    \n    estatutos   : llamada SCOLON\n                | asignacion SCOLON\n                | returnf SCOLON\n                | lectura SCOLON\n                | escritura SCOLON\n                | condicion\n                | cond_w\n                | cond_f\n    \n    asignacion  : idCall ASIGNA exp \n    \n    llamada   : ID DOT ID LPAREN enviaReferencia RPAREN\n              | ID LPAREN enviaReferencia RPAREN \n    \n    enviaReferencia   : exp\n                      | exp COMMA enviaReferencia\n                      | empty\n    \n    returnf   : RETURN LPAREN exp RPAREN \n    \n    lectura   : READ LPAREN idCall RPAREN\n    \n    escritura   : WRITE LPAREN exp lextra RPAREN\n                | WRITE LPAREN LETRERO lextra RPAREN\n    \n    lextra  : COMMA exp lextra\n            | COMMA LETRERO lextra\n            | empty\n    \n    condicion   : IF LPAREN exp RPAREN THEN LBRACE listaEstatutos RBRACE\n                | IF LPAREN exp RPAREN THEN LBRACE listaEstatutos RBRACE ELSE LBRACE listaEstatutos RBRACE\n    \n    cond_w : WHILE LPAREN exp RPAREN DO LBRACE listaEstatutos RBRACE\n    \n    cond_f : FOR idCall ASIGNA exp TO exp DO LBRACE listaEstatutos RBRACE\n    \n    exp     : texp\n            | texp OR exp\n    \n    texp    : gexp\n            | gexp AND texp\n    \n    gexp    : mexp\n            | mexp LT mexp\n            | mexp GT mexp\n            | mexp EQUALS mexp\n            | mexp NEQUALS mexp\n    \n    mexp    : t\n            | t PLUS mexp\n            | t MINUS mexp\n    \n    t   : f\n        | f MULT t\n        | f DIV t\n    \n    f   : LPAREN exp RPAREN\n        | CTE_I\n        | CTE_F\n        | CTE_C\n        | llamada\n        | idCall\n    \n    empty :\n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,129,],[0,-1,]),'ID':([2,6,9,26,27,28,29,31,47,53,56,58,59,61,62,63,64,65,66,67,68,69,70,76,86,99,101,108,109,110,117,119,120,121,123,131,132,133,134,135,136,137,138,139,140,141,150,151,159,160,168,175,182,187,188,195,196,197,198,203,204,207,],[3,11,21,33,35,21,40,54,40,21,21,82,40,40,40,40,40,40,40,40,40,40,40,40,40,35,40,-38,-39,-40,21,21,35,40,40,-33,-34,-35,-36,-37,40,40,21,40,40,40,163,21,40,40,40,21,40,40,40,40,-54,-56,40,40,-57,-55,]),'SCOLON':([3,34,35,36,37,38,40,42,43,44,45,46,48,49,50,51,52,60,87,88,89,90,91,92,93,94,95,96,97,103,104,105,106,107,122,128,148,152,161,165,166,176,179,],[4,57,-13,-14,-15,-16,-10,-58,-60,-62,-67,-70,-74,-75,-76,-77,-78,-11,-59,-61,-63,-64,-65,-66,-68,-69,-71,-72,-73,131,132,133,134,135,-43,151,-12,-41,-42,-47,-48,-49,-50,]),'CLASS':([4,149,],[6,6,]),'VAR':([4,5,7,57,118,149,162,],[-79,9,-3,9,9,-79,-2,]),'VOID':([4,5,7,8,10,57,81,98,149,162,183,202,],[-79,-79,-3,15,-28,-79,-27,15,-79,-2,15,15,]),'INT':([4,5,7,8,10,27,57,81,98,99,120,149,162,183,202,],[-79,-79,-3,16,-28,36,-79,-27,16,36,36,-79,-2,16,16,]),'FLOAT':([4,5,7,8,10,27,57,81,98,99,120,149,162,183,202,],[-79,-79,-3,17,-28,37,-79,-27,17,37,37,-79,-2,17,17,]),'CHAR':([4,5,7,8,10,27,57,81,98,99,120,149,162,183,202,],[-79,-79,-3,18,-28,38,-79,-27,18,38,38,-79,-2,18,18,]),'MAIN':([4,5,7,8,10,12,14,57,81,149,162,183,190,],[-79,-79,-3,-79,-28,25,-30,-79,-27,-79,-2,-79,-29,]),'LBRACE':([10,11,22,24,55,57,75,81,118,143,180,181,191,194,200,],[-28,-79,30,-5,76,-79,-4,-27,-79,160,187,188,195,198,203,]),'LT':([11,40,44,45,46,48,49,50,51,52,60,93,94,95,96,97,122,148,161,],[23,-10,63,-67,-70,-74,-75,-76,-77,-78,-11,-68,-69,-71,-72,-73,-43,-12,-42,]),'FUNC':([13,15,16,17,18,126,],[26,-19,-20,-21,-22,150,]),'COLON':([19,20,21,39,60,73,80,148,],[27,-8,-10,-9,-11,99,120,-12,]),'COMMA':([20,21,35,36,37,38,40,42,43,44,45,46,48,49,50,51,52,60,78,84,87,88,89,90,91,92,93,94,95,96,97,122,145,148,155,156,161,177,178,],[28,-10,-13,-14,-15,-16,-10,-58,-60,-62,-67,-70,-74,-75,-76,-77,-78,-11,119,123,-59,-61,-63,-64,-65,-66,-68,-69,-71,-72,-73,-43,-26,-12,168,168,-42,168,168,]),'ASIGNA':([21,40,60,111,142,148,],[-10,-10,-11,136,159,-12,]),'RPAREN':([21,32,35,36,37,38,40,42,43,44,45,46,48,49,50,51,52,56,59,60,71,77,78,79,83,84,85,87,88,89,90,91,92,93,94,95,96,97,119,121,122,123,144,145,146,147,148,153,154,155,156,157,158,161,167,169,170,175,177,178,184,185,186,],[-10,55,-13,-14,-15,-16,-10,-58,-60,-62,-67,-70,-74,-75,-76,-77,-78,-79,-79,-11,97,118,-23,-25,122,-44,-46,-59,-61,-63,-64,-65,-66,-68,-69,-71,-72,-73,-79,-79,-43,-79,-24,-26,161,-45,-12,165,166,-79,-79,171,172,-42,176,-53,179,-79,-79,-79,191,-51,-52,]),'LBRACK':([21,40,60,],[29,29,86,]),'EXTENDS':([23,],[31,]),'LPAREN':([25,29,33,40,47,59,61,62,63,64,65,66,67,68,69,70,82,86,112,113,114,115,116,121,123,136,137,139,140,141,159,163,168,182,],[32,47,56,59,47,47,47,47,47,47,47,47,47,47,47,47,121,47,137,138,139,140,141,47,47,47,47,47,47,47,47,175,47,47,]),'CTE_I':([29,47,59,61,62,63,64,65,66,67,68,69,70,86,121,123,136,137,139,140,141,159,168,182,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'CTE_F':([29,47,59,61,62,63,64,65,66,67,68,69,70,86,121,123,136,137,139,140,141,159,168,182,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'CTE_C':([29,47,59,61,62,63,64,65,66,67,68,69,70,86,121,123,136,137,139,140,141,159,168,182,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'ATTRIBUTES':([30,],[53,]),'DOT':([40,],[58,]),'MULT':([40,46,48,49,50,51,52,60,97,122,148,161,],[-10,69,-74,-75,-76,-77,-78,-11,-73,-43,-12,-42,]),'DIV':([40,46,48,49,50,51,52,60,97,122,148,161,],[-10,70,-74,-75,-76,-77,-78,-11,-73,-43,-12,-42,]),'PLUS':([40,45,46,48,49,50,51,52,60,95,96,97,122,148,161,],[-10,67,-70,-74,-75,-76,-77,-78,-11,-71,-72,-73,-43,-12,-42,]),'MINUS':([40,45,46,48,49,50,51,52,60,95,96,97,122,148,161,],[-10,68,-70,-74,-75,-76,-77,-78,-11,-71,-72,-73,-43,-12,-42,]),'GT':([40,44,45,46,48,49,50,51,52,54,60,93,94,95,96,97,122,148,161,],[-10,64,-67,-70,-74,-75,-76,-77,-78,75,-11,-68,-69,-71,-72,-73,-43,-12,-42,]),'EQUALS':([40,44,45,46,48,49,50,51,52,60,93,94,95,96,97,122,148,161,],[-10,65,-67,-70,-74,-75,-76,-77,-78,-11,-68,-69,-71,-72,-73,-43,-12,-42,]),'NEQUALS':([40,44,45,46,48,49,50,51,52,60,93,94,95,96,97,122,148,161,],[-10,66,-67,-70,-74,-75,-76,-77,-78,-11,-68,-69,-71,-72,-73,-43,-12,-42,]),'AND':([40,43,44,45,46,48,49,50,51,52,60,89,90,91,92,93,94,95,96,97,122,148,161,],[-10,62,-62,-67,-70,-74,-75,-76,-77,-78,-11,-63,-64,-65,-66,-68,-69,-71,-72,-73,-43,-12,-42,]),'OR':([40,42,43,44,45,46,48,49,50,51,52,60,88,89,90,91,92,93,94,95,96,97,122,148,161,],[-10,61,-60,-62,-67,-70,-74,-75,-76,-77,-78,-11,-61,-63,-64,-65,-66,-68,-69,-71,-72,-73,-43,-12,-42,]),'RBRACK':([40,41,42,43,44,45,46,48,49,50,51,52,60,87,88,89,90,91,92,93,94,95,96,97,122,124,148,161,],[-10,60,-58,-60,-62,-67,-70,-74,-75,-76,-77,-78,-11,-59,-61,-63,-64,-65,-66,-68,-69,-71,-72,-73,-43,148,-12,-42,]),'TO':([40,42,43,44,45,46,48,49,50,51,52,60,87,88,89,90,91,92,93,94,95,96,97,122,148,161,173,],[-10,-58,-60,-62,-67,-70,-74,-75,-76,-77,-78,-11,-59,-61,-63,-64,-65,-66,-68,-69,-71,-72,-73,-43,-12,-42,182,]),'DO':([40,42,43,44,45,46,48,49,50,51,52,60,87,88,89,90,91,92,93,94,95,96,97,122,148,161,172,189,],[-10,-58,-60,-62,-67,-70,-74,-75,-76,-77,-78,-11,-59,-61,-63,-64,-65,-66,-68,-69,-71,-72,-73,-43,-12,-42,181,194,]),'METHODS':([53,72,74,151,164,],[-79,98,-7,-79,-6,]),'RBRACE':([76,98,100,101,102,108,109,110,125,127,130,131,132,133,134,135,160,174,187,188,192,193,195,196,197,198,199,201,202,203,204,205,206,207,],[-79,-79,129,-79,-32,-38,-39,-40,149,-18,-31,-33,-34,-35,-36,-37,-79,183,-79,-79,196,197,-79,-54,-56,-79,202,204,-79,-79,-57,-17,207,-55,]),'RETURN':([76,101,108,109,110,131,132,133,134,135,160,187,188,195,196,197,198,203,204,207,],[112,112,-38,-39,-40,-33,-34,-35,-36,-37,112,112,112,112,-54,-56,112,112,-57,-55,]),'READ':([76,101,108,109,110,131,132,133,134,135,160,187,188,195,196,197,198,203,204,207,],[113,113,-38,-39,-40,-33,-34,-35,-36,-37,113,113,113,113,-54,-56,113,113,-57,-55,]),'WRITE':([76,101,108,109,110,131,132,133,134,135,160,187,188,195,196,197,198,203,204,207,],[114,114,-38,-39,-40,-33,-34,-35,-36,-37,114,114,114,114,-54,-56,114,114,-57,-55,]),'IF':([76,101,108,109,110,131,132,133,134,135,160,187,188,195,196,197,198,203,204,207,],[115,115,-38,-39,-40,-33,-34,-35,-36,-37,115,115,115,115,-54,-56,115,115,-57,-55,]),'WHILE':([76,101,108,109,110,131,132,133,134,135,160,187,188,195,196,197,198,203,204,207,],[116,116,-38,-39,-40,-33,-34,-35,-36,-37,116,116,116,116,-54,-56,116,116,-57,-55,]),'FOR':([76,101,108,109,110,131,132,133,134,135,160,187,188,195,196,197,198,203,204,207,],[117,117,-38,-39,-40,-33,-34,-35,-36,-37,117,117,117,117,-54,-56,117,117,-57,-55,]),'LETRERO':([139,168,],[156,178,]),'THEN':([171,],[180,]),'ELSE':([196,],[200,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declarClases':([4,149,],[5,162,]),'empty':([4,5,8,11,53,56,57,59,76,98,101,118,119,121,123,149,151,155,156,160,175,177,178,183,187,188,195,198,202,203,],[7,10,14,24,74,79,10,85,102,127,102,10,79,85,85,7,74,169,169,102,79,169,169,14,102,102,102,102,127,102,]),'declarVar':([5,57,118,],[8,81,143,]),'definFunc':([8,183,],[12,190,]),'tipoMethod':([8,98,183,202,],[13,126,13,126,]),'listaId':([9,28,53,151,],[19,39,73,73,]),'idCall':([9,28,29,47,53,56,59,61,62,63,64,65,66,67,68,69,70,76,86,101,117,119,121,123,136,137,138,139,140,141,151,159,160,168,175,182,187,188,195,198,203,],[20,20,52,52,20,80,52,52,52,52,52,52,52,52,52,52,52,111,52,111,142,80,52,52,52,52,154,52,52,52,20,52,111,52,80,52,111,111,111,111,111,]),'herencia':([11,],[22,]),'tipo':([27,99,120,],[34,128,145,]),'exp':([29,47,59,61,86,121,123,136,137,139,140,141,159,168,182,],[41,71,84,87,124,84,84,152,153,155,157,158,173,177,189,]),'texp':([29,47,59,61,62,86,121,123,136,137,139,140,141,159,168,182,],[42,42,42,42,88,42,42,42,42,42,42,42,42,42,42,42,]),'gexp':([29,47,59,61,62,86,121,123,136,137,139,140,141,159,168,182,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'mexp':([29,47,59,61,62,63,64,65,66,67,68,86,121,123,136,137,139,140,141,159,168,182,],[44,44,44,44,44,89,90,91,92,93,94,44,44,44,44,44,44,44,44,44,44,44,]),'t':([29,47,59,61,62,63,64,65,66,67,68,69,70,86,121,123,136,137,139,140,141,159,168,182,],[45,45,45,45,45,45,45,45,45,45,45,95,96,45,45,45,45,45,45,45,45,45,45,45,]),'f':([29,47,59,61,62,63,64,65,66,67,68,69,70,86,121,123,136,137,139,140,141,159,168,182,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'llamada':([29,47,59,61,62,63,64,65,66,67,68,69,70,76,86,101,121,123,136,137,139,140,141,159,160,168,182,187,188,195,198,203,],[51,51,51,51,51,51,51,51,51,51,51,51,51,103,51,103,51,51,51,51,51,51,51,51,103,51,51,103,103,103,103,103,]),'declarAttributes':([53,151,],[72,164,]),'listaParam':([56,119,175,],[77,144,184,]),'param':([56,119,175,],[78,78,78,]),'enviaReferencia':([59,121,123,],[83,146,147,]),'listaEstatutos':([76,101,160,187,188,195,198,203,],[100,130,174,192,193,199,201,206,]),'estatutos':([76,101,160,187,188,195,198,203,],[101,101,101,101,101,101,101,101,]),'asignacion':([76,101,160,187,188,195,198,203,],[104,104,104,104,104,104,104,104,]),'returnf':([76,101,160,187,188,195,198,203,],[105,105,105,105,105,105,105,105,]),'lectura':([76,101,160,187,188,195,198,203,],[106,106,106,106,106,106,106,106,]),'escritura':([76,101,160,187,188,195,198,203,],[107,107,107,107,107,107,107,107,]),'condicion':([76,101,160,187,188,195,198,203,],[108,108,108,108,108,108,108,108,]),'cond_w':([76,101,160,187,188,195,198,203,],[109,109,109,109,109,109,109,109,]),'cond_f':([76,101,160,187,188,195,198,203,],[110,110,110,110,110,110,110,110,]),'declarMethods':([98,202,],[125,205,]),'lextra':([155,156,177,178,],[167,170,185,186,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SCOLON declarClases declarVar definFunc MAIN LPAREN RPAREN LBRACE listaEstatutos RBRACE','program',12,'p_program','parser.py',18),
  ('declarClases -> CLASS ID herencia LBRACE ATTRIBUTES declarAttributes METHODS declarMethods RBRACE declarClases','declarClases',10,'p_declarClases','parser.py',23),
  ('declarClases -> empty','declarClases',1,'p_declarClases','parser.py',24),
  ('herencia -> LT EXTENDS ID GT','herencia',4,'p_herencia','parser.py',28),
  ('herencia -> empty','herencia',1,'p_herencia','parser.py',29),
  ('declarAttributes -> listaId COLON tipo SCOLON declarAttributes','declarAttributes',5,'p_declarAttributes','parser.py',33),
  ('declarAttributes -> empty','declarAttributes',1,'p_declarAttributes','parser.py',34),
  ('listaId -> idCall','listaId',1,'p_listaId','parser.py',38),
  ('listaId -> idCall COMMA listaId','listaId',3,'p_listaId','parser.py',39),
  ('idCall -> ID','idCall',1,'p_idCall','parser.py',43),
  ('idCall -> ID LBRACK exp RBRACK','idCall',4,'p_idCall','parser.py',44),
  ('idCall -> ID LBRACK exp RBRACK LBRACK exp RBRACK','idCall',7,'p_idCall','parser.py',45),
  ('tipo -> ID','tipo',1,'p_tipo','parser.py',49),
  ('tipo -> INT','tipo',1,'p_tipo','parser.py',50),
  ('tipo -> FLOAT','tipo',1,'p_tipo','parser.py',51),
  ('tipo -> CHAR','tipo',1,'p_tipo','parser.py',52),
  ('declarMethods -> tipoMethod FUNC ID LPAREN listaParam RPAREN LBRACE listaEstatutos RBRACE declarMethods','declarMethods',10,'p_declarMethods','parser.py',56),
  ('declarMethods -> empty','declarMethods',1,'p_declarMethods','parser.py',57),
  ('tipoMethod -> VOID','tipoMethod',1,'p_tipoMethod','parser.py',61),
  ('tipoMethod -> INT','tipoMethod',1,'p_tipoMethod','parser.py',62),
  ('tipoMethod -> FLOAT','tipoMethod',1,'p_tipoMethod','parser.py',63),
  ('tipoMethod -> CHAR','tipoMethod',1,'p_tipoMethod','parser.py',64),
  ('listaParam -> param','listaParam',1,'p_listaParam','parser.py',68),
  ('listaParam -> param COMMA listaParam','listaParam',3,'p_listaParam','parser.py',69),
  ('listaParam -> empty','listaParam',1,'p_listaParam','parser.py',70),
  ('param -> idCall COLON tipo','param',3,'p_param','parser.py',74),
  ('declarVar -> VAR listaId COLON tipo SCOLON declarVar','declarVar',6,'p_declarVar','parser.py',78),
  ('declarVar -> empty','declarVar',1,'p_declarVar','parser.py',79),
  ('definFunc -> tipoMethod FUNC ID LPAREN listaParam RPAREN declarVar LBRACE listaEstatutos RBRACE definFunc','definFunc',11,'p_definFunc','parser.py',83),
  ('definFunc -> empty','definFunc',1,'p_definFunc','parser.py',84),
  ('listaEstatutos -> estatutos listaEstatutos','listaEstatutos',2,'p_listaEstatutos','parser.py',88),
  ('listaEstatutos -> empty','listaEstatutos',1,'p_listaEstatutos','parser.py',89),
  ('estatutos -> llamada SCOLON','estatutos',2,'p_estatutos','parser.py',104),
  ('estatutos -> asignacion SCOLON','estatutos',2,'p_estatutos','parser.py',105),
  ('estatutos -> returnf SCOLON','estatutos',2,'p_estatutos','parser.py',106),
  ('estatutos -> lectura SCOLON','estatutos',2,'p_estatutos','parser.py',107),
  ('estatutos -> escritura SCOLON','estatutos',2,'p_estatutos','parser.py',108),
  ('estatutos -> condicion','estatutos',1,'p_estatutos','parser.py',109),
  ('estatutos -> cond_w','estatutos',1,'p_estatutos','parser.py',110),
  ('estatutos -> cond_f','estatutos',1,'p_estatutos','parser.py',111),
  ('asignacion -> idCall ASIGNA exp','asignacion',3,'p_asignacion','parser.py',115),
  ('llamada -> ID DOT ID LPAREN enviaReferencia RPAREN','llamada',6,'p_llamada','parser.py',119),
  ('llamada -> ID LPAREN enviaReferencia RPAREN','llamada',4,'p_llamada','parser.py',120),
  ('enviaReferencia -> exp','enviaReferencia',1,'p_enviaReferencia','parser.py',124),
  ('enviaReferencia -> exp COMMA enviaReferencia','enviaReferencia',3,'p_enviaReferencia','parser.py',125),
  ('enviaReferencia -> empty','enviaReferencia',1,'p_enviaReferencia','parser.py',126),
  ('returnf -> RETURN LPAREN exp RPAREN','returnf',4,'p_returnf','parser.py',130),
  ('lectura -> READ LPAREN idCall RPAREN','lectura',4,'p_lectura','parser.py',134),
  ('escritura -> WRITE LPAREN exp lextra RPAREN','escritura',5,'p_escritura','parser.py',138),
  ('escritura -> WRITE LPAREN LETRERO lextra RPAREN','escritura',5,'p_escritura','parser.py',139),
  ('lextra -> COMMA exp lextra','lextra',3,'p_lextra','parser.py',143),
  ('lextra -> COMMA LETRERO lextra','lextra',3,'p_lextra','parser.py',144),
  ('lextra -> empty','lextra',1,'p_lextra','parser.py',145),
  ('condicion -> IF LPAREN exp RPAREN THEN LBRACE listaEstatutos RBRACE','condicion',8,'p_condicion','parser.py',149),
  ('condicion -> IF LPAREN exp RPAREN THEN LBRACE listaEstatutos RBRACE ELSE LBRACE listaEstatutos RBRACE','condicion',12,'p_condicion','parser.py',150),
  ('cond_w -> WHILE LPAREN exp RPAREN DO LBRACE listaEstatutos RBRACE','cond_w',8,'p_cond_w','parser.py',154),
  ('cond_f -> FOR idCall ASIGNA exp TO exp DO LBRACE listaEstatutos RBRACE','cond_f',10,'p_cond_f','parser.py',158),
  ('exp -> texp','exp',1,'p_exp','parser.py',162),
  ('exp -> texp OR exp','exp',3,'p_exp','parser.py',163),
  ('texp -> gexp','texp',1,'p_texp','parser.py',167),
  ('texp -> gexp AND texp','texp',3,'p_texp','parser.py',168),
  ('gexp -> mexp','gexp',1,'p_gexp','parser.py',172),
  ('gexp -> mexp LT mexp','gexp',3,'p_gexp','parser.py',173),
  ('gexp -> mexp GT mexp','gexp',3,'p_gexp','parser.py',174),
  ('gexp -> mexp EQUALS mexp','gexp',3,'p_gexp','parser.py',175),
  ('gexp -> mexp NEQUALS mexp','gexp',3,'p_gexp','parser.py',176),
  ('mexp -> t','mexp',1,'p_mexp','parser.py',180),
  ('mexp -> t PLUS mexp','mexp',3,'p_mexp','parser.py',181),
  ('mexp -> t MINUS mexp','mexp',3,'p_mexp','parser.py',182),
  ('t -> f','t',1,'p_t','parser.py',186),
  ('t -> f MULT t','t',3,'p_t','parser.py',187),
  ('t -> f DIV t','t',3,'p_t','parser.py',188),
  ('f -> LPAREN exp RPAREN','f',3,'p_f','parser.py',192),
  ('f -> CTE_I','f',1,'p_f','parser.py',193),
  ('f -> CTE_F','f',1,'p_f','parser.py',194),
  ('f -> CTE_C','f',1,'p_f','parser.py',195),
  ('f -> llamada','f',1,'p_f','parser.py',196),
  ('f -> idCall','f',1,'p_f','parser.py',197),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',201),
]
