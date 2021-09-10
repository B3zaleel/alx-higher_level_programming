#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: The pointer to the head of the linked list
 *
 * Return: 1 if the linked list is a palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	int *vals = NULL, len = 0, i = 0, j = 0, stop = 0, res = 1;
	listint_t *node = NULL;

	if (head != NULL)
	{
		node = *head;
		while (node != NULL)
			node = node->next, len++;
		vals = malloc(sizeof(int) * len);
		if (vals != NULL)
		{
			node = *head;
			while (node != NULL)
				*(vals + i) = node->n, node = node->next, i++;
			j = len - 1, i = 0;
			while ((i < len / 2) && !stop)
			{
				if (*(vals + i) == *(vals + j))
					i++, j--;
				else
					res = 0, stop = 1;
			}
			free(vals);
		}
	}
	return (res);
}
