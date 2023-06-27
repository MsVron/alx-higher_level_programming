#include <Python.h>
#include <stdio.h>
#include <string.h>

/**
 *print_python_list - Prints information about a Python list object
 *@p: Pointer to the PyObject representing the list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject * item;

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid PyListObject\n");
		return;
	}

	size = Py_SIZE(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject*) p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 *print_python_bytes - Prints information about a Python bytes object
 *@p: Pointer to the PyObject representing the bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *bytes;
	char printable;
	PyObject * repr;

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid PyBytesObject\n");
		return;
	}

	size = PyBytes_Size(p);
	bytes = PyBytes_AsString(p);

	printf("[.] Bytes object info\n");
	printf(" [.] Size: %ld\n", size);
	printf(" [.] Trying string: %s\n", bytes);

	if (size > 10)
		size = 10;

	printf(" [.] First %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printable = bytes[i];
		if (printable < 32 || printable >= 127)
			printable = '.';
		printf("%02x%c", bytes[i] &0xff, i < size - 1 ? ' ' : '\n');
	}

	repr = PyObject_Repr(p);
	printf(" [.] Address of PyBytes object: %p\n", (void*) p);
	printf(" [.] Bytes object printed: %s\n", PyUnicode_AsUTF8(repr));
	Py_DECREF(repr);
}

/**
 *print_python_float - Prints information about a Python float object
 *@p: Pointer to the PyObject representing the float object
 */
void print_python_float(PyObject *p)
{
	double value;
	char *str_value;

	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid PyFloatObject\n");
		return;
	}

	value = PyFloat_AsDouble(p);
	str_value = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);

	printf("[.] Float object info\n");
	printf(" [.] Value: %s\n", str_value);

	PyMem_Free(str_value);
}
