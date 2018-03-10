_input_chars = ["u''''", "u''", "u'", "o''''", "o''", "o'", "i'", "e'", "a'"]
_output_chars = ['ű', 'ü', 'ú', 'ő', 'ö', 'ó', 'í', 'é', 'á']
_n_of_v = 9
_yes_set = set(('y','yes','ye'))
_no_set = set(('n', 'no'))
_exit_set = set(('\exit', '\quit', '\q', '\e'))
#_input = set(('\\n',"\\new"))
_back = set(('\\back','\\b'))
_test_set =  set(("\\test", "\\t",))
_input_mode_set = set(("\input", "\i", "\\n", "\\new"))
_delete_set = set(('\delete', '\d', '\del'))

_correct_question_2p = '"{}" in english means: "{}", is it correct? Type Y[es]/N[o]]: '
_welcome_screen = """
Welcome to the learning tool!"""

_main_menu = """
Type:
        \"\\test" to start a test
        \"\\new" to insert a new word and its meaning
        \"\\q" to QUIT
        \"\\del" to delete a term
:"""
