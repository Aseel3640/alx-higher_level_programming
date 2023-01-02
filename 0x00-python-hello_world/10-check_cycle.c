#include "lists.h"
#include <string.h>
/**
 * check_cycle - entry point
 * desc: check_cycle function
 * @list: pointer to list_t
 * Return: singly linked list cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *j, *i;

	j = list;
	i = list;

	while (j && i && i->next)
	{
		j = j->next;
		i = i->next->next;
		if (j == i)
			return (1);
	}
	return (0);
}

