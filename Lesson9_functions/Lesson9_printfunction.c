static PyObject *
builtin_print(PyObject *self, PyObject *args, PyObject *kwds)
{
    static char *kwlist[] = {"sep", "end", "file", 0};
    static PyObject *dummy_args = NULL;
    static PyObject *unicode_newline = NULL, *unicode_space = NULL;
    static PyObject *str_newline = NULL, *str_space = NULL;
    PyObject *newline, *space;
    PyObject *sep = NULL, *end = NULL, *file = NULL;
    int i, err, use_unicode = 0;

    if (dummy_args == NULL) {
        if (!(dummy_args = PyTuple_New(0)))
            return NULL;
    }
    if (str_newline == NULL) {
        str_newline = PyString_FromString("\n");
        if (str_newline == NULL)
            return NULL;
        str_space = PyString_FromString(" ");
        if (str_space == NULL) {
            Py_CLEAR(str_newline);
            return NULL;
        }
#ifdef Py_USING_UNICODE
        unicode_newline = PyUnicode_FromString("\n");
        if (unicode_newline == NULL) {
            Py_CLEAR(str_newline);
            Py_CLEAR(str_space);
            return NULL;
        }
        unicode_space = PyUnicode_FromString(" ");
        if (unicode_space == NULL) {
            Py_CLEAR(str_newline);
            Py_CLEAR(str_space);
            Py_CLEAR(unicode_space);
            return NULL;
        }
#endif
