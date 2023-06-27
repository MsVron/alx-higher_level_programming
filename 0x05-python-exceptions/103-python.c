#include <Python.h>
#include <stdio.h>
#include <string.h>

/**
 *print_python_list - Prints information about a Python list object
 *@p: Pointer to the PyObject representing the list
 */
void print_python_list(PyObject *p)
{
	setbuf(stdout, NULL);

	Py_ssize_t size, i;
	PyObject * item;

	if (!p || !PyList_Check(p))
	{
		printf("[ERROR] Invalid PyListObject\n");
		return;
	}

	size = PyObject_Length(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyVarObject*) p)->ob_size);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
	}
}

/**
 *print_python_bytes - Prints information about a Python bytes object
 *@p: Pointer to the PyObject representing the bytes object
 */
void print_python_bytes(PyObject *p)
{
	setbuf(stdout, NULL);

	Py_ssize_t size, i;
	char *bytes;
	char printable;

	if (!p || !PyBytes_Check(p))
	{
		printf("[ERROR] Invalid PyBytesObject\n");
		return;
	}

	size = PyObject_Length(p);
	bytes = PyBytes_AsString(p);

	printf("[.] Bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes);

	printf("  first %ld bytes: ", size> 10 ? 10 : size);
	for (i = 0; i < size && i < 10; i++)
	{
		printable = bytes[i];
		if (printable < 32 || printable >= 127)
			printable = '.';
		printf("%02x%c", bytes[i] &0xff, i < size - 1 ? ' ' : '\n');
	}
}

/**
 *print_python_float - Prints information about a Python float object
 *@p: Pointer to the PyObject representing the float object
 */
void print_python_float(PyObject *p)
{
	setbuf(stdout, NULL);

	double value;
	char *str_value;

	if (!p || !PyFloat_Check(p))
	{
		printf("[ERROR] Invalid PyFloatObject\n");
		return;
	}

	value = ((PyFloatObject*) p)->ob_fval;
	str_value = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);

	printf("[.] Float object info\n");
	printf("  value: %s\n", str_value);

	PyMem_Free(str_value);
}
