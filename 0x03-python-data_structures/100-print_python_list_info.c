#include <Python.h>
#include <stdio.h>

void print_python_list_info(pyObject *p)
{
    py_ssize_t size, allocated, i;
    pyObject *obj;

    size = PyList_Size(p);
    allocated = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python Lisr = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    for(i = 0; i < size; ++i)
    {
        obj = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(obj)->tp_name);
    }
}