#include <stdio.h>
#include <sys/types.h>
#include <python3.8/object.h>
#include <python3.8/listobject.h>

/**
 * print_python_list_info - Prints some basic info about a Python list object
 * @p: A pointer to the Python list object
 */
void print_python_list_info(PyObject *p)
{
	int i, list_len;

	list_len = (int)PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", list_len);
	printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);
	for (i = 0; i < list_len; i++)
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
