#include "lists.h"

/**
* print_dlistint - print nodes in a linked list
* @h: pointer to linked list
* Return: number of nodes in a linked list
*/

size_t print_dlistint(const dlistint_t *h)
{
	size_t count = 0;

	while (h != NULL)
	{
		count++;
		printf("%d\n", h->n);
		h = h->next;
	}
	return (count);
}
