#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <python3.4/Python.h>
#include <python3.4/object.h>
#include <python3.4/listobject.h>
#include <python3.4/listobject.h>
#define PY_SSIZE_T_CLEAN

/**
 * print_python_bytes - Prints some basic info about a Python bytes object
 * @p: A pointer to the Python bytes object
 */
void print_python_bytes(PyObject *p)
{
    int i, bytes_len, n;

    printf("[.] bytes object info\n");
    if (p != NULL
        && p->ob_type != NULL
        && (p->ob_type)->tp_name != NULL
        && *((p->ob_type)->tp_name + 0) == 'b'
        && *((p->ob_type)->tp_name + 1) == 'y'
        && *((p->ob_type)->tp_name + 2) == 't'
        && *((p->ob_type)->tp_name + 3) == 'e'
        && *((p->ob_type)->tp_name + 4) == 's')
    {
        bytes_len = (int)(((PyVarObject *)(p))->ob_size);
        n = bytes_len < 10 ? bytes_len : 9;
        printf("  size: %d\n", bytes_len);
        printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);
        if (n > 0)
        {
            printf("  first %d bytes:", n + 1);
            for (i = 0; i < n + 1; i++)
            {
                printf(" %02x", (unsigned char)*(((PyBytesObject *)p)->ob_sval + i));
            }
            printf("\n");
        }
    }
    else
    {
        printf("  [ERROR] Invalid Bytes Object\n");
    }
}

/**
 * print_python_list - Prints some basic info about a Python list object
 * @p: A pointer to the Python list object
 */
void print_python_list(PyObject *p)
{
	int i, list_len;
    PyObject *item = NULL;

    printf("[*] Python list info\n");
    if (p != NULL
        && p->ob_type != NULL
        && (p->ob_type)->tp_name != NULL
        && *((p->ob_type)->tp_name + 0) == 'l'
        && *((p->ob_type)->tp_name + 1) == 'i'
        && *((p->ob_type)->tp_name + 2) == 's'
        && *((p->ob_type)->tp_name + 3) == 't')
    {
        list_len = (int)(((PyVarObject *)(p))->ob_size);
        printf("[*] Size of the Python List = %d\n", list_len);
        printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);
        for (i = 0; i < list_len; i++)
        {
            item = (PyObject *)*(((PyListObject *)p)->ob_item + i);
            printf("Element %d: %s\n", i, (item->ob_type)->tp_name);
			if (item != NULL
				&& item->ob_type != NULL
				&& (item->ob_type)->tp_name != NULL
				&& *((item->ob_type)->tp_name + 0) == 'b'
				&& *((item->ob_type)->tp_name + 1) == 'y'
				&& *((item->ob_type)->tp_name + 2) == 't'
				&& *((item->ob_type)->tp_name + 3) == 'e'
				&& *((item->ob_type)->tp_name + 4) == 's')
			{
				print_python_bytes(item);
			}
        }
    }
    else
    {
        printf("  [ERROR] Invalid List Object\n");
    }
}
