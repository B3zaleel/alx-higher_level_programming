#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: The pointer to the head of the linked list
 *
 * Return: 1 if the linked list is a palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	int len = 0, i = 0, stop = 0, res = 1;
	listint_t *node0, *node1 = NULL, *next = NULL, *tmp = NULL, *prev = NULL;

	if ((head != NULL) && (*head != NULL))
	{
		node0 = *head;
		while (node0 != NULL)
			node0 = node0->next, len++;
		node0 = *head, node1 = *head;
		while ((i < len) && !stop)
		{
			if (i >= (len / 2))
			{
				next = (i == len / 2 ? node1 : next);
				if ((len % 2 != 0) && (i == len / 2))
				{
					node1 = node1->next, i++;
					continue;
				}
				if (node0->n != node1->n)
					res = 0, stop = 1;
				if (node0->n == node1->n)
					node0 = node0->next, node1 = node1->next, i++;
			}
			else
			{
				node1 = node1->next;
				next = node0->next, node0->next = prev, prev = node0;
				node0 = ((i < (len / 2 - 1)) ? next : node0), tmp = node0;
				i++;
			}
		}
		for (i = 0; i < (len / 2); i++)
			next = i == 0 ? next : prev, prev = tmp, tmp = tmp->next, prev->next = next;
	}
	return (res);
}
