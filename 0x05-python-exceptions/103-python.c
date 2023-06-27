#include <Python.h>
#include <stdio.h>
#include <string.h>

/**
 *print_python_list - Prints basic information about Python lists
 *@p: Pointer to a PyObject representing a list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid PyListObject\n");
		return;
	}

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject*) p)->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}

/**
 *print_python_bytes - Prints basic information about Python bytes objects
 *@p: Pointer to a PyObject representing a bytes object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid PyBytesObject\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("[*] Python bytes info\n");
	printf("[*] Size of the bytes object = %ld\n", size);
	printf("Bytes object contents: ");

	if (size > 10)
		size = 10;

	str = PyBytes_AsString(p);
	printf("'");
	for (i = 0; i < size; i++)
	{
		if (str[i] >= 0 && str[i] <= 31)
			printf("\\x%.2x", (unsigned char) str[i]);
		else
			printf("%c", str[i]);
	}

	printf("'\n");
}

/**
 *print_python_float - Prints basic information about Python float objects
 *@p: Pointer to a PyObject representing a float object
 */
void print_python_float(PyObject *p)
{
	double value;

	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid PyFloatObject\n");
		return;
	}

	printf("[*] Python float info\n");
	value = PyFloat_AsDouble(p);
	printf("Value: %f\n", value);
}
