#include "lists.h"
#include <stdlib.h>

/**
 * delete_dnodeint_at_index - delete the node at index of a dlistint_t list
 *
 * @head: double pointer to the list
 * @index: index of the node to delete
 *
 * Return: 1 if it succeeded, -1 if it failed
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *saved_head;
	dlistint_t *tmp;
	unsigned int i;

	if (*head == NULL)
		return (-1);

	saved_head = *head;
	i = 0;

	while (saved_head != NULL && i < index)
	{
		saved_head = saved_head->next;
		i++;
	}

	if (saved_head == NULL)
		return (-1);

	if (index == 0)
	{
		*head = saved_head->next;
		if (*head != NULL)
			(*head)->prev = NULL;
		free(saved_head);
		return (1);
	}

	tmp = saved_head->prev;
	tmp->next = saved_head->next;
	if (saved_head->next != NULL)
		saved_head->next->prev = tmp;
	free(saved_head);

	return (1);
}
