#include "lists.h"
/**
 * insert_node - function, inserts a number into a sorted singly linked list.
 * @head: head of linked list
 * @number: number to insert
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = NULL;
	listint_t *new_node = NULL;

	if (head == NULL)
		return (NULL);
	current = *head;
	new_node = malloc(sizeof(listint_t));
	new_node->n = number;
	new_node->next = NULL;
	if (current == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	if (number < current->n)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}
	while (current->next && current->next->n <= number)
		current = current->next;
	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}