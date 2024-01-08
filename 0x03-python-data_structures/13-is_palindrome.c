#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * reverseList - functio to reverse a linked list
 * @head: pointer to head node
 * Return: Nothing
 */
void reverseList(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
/**
 * ispalindrome - function to check if a linkd list is a palindrome
 * @head: pointer to headnode
 * Return: 1 if palindrome 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (-1);
	listint_t *slow = *head, *fast = *head, *temp = *head,
	*dup = NULL;

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}

		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}
	reverseList(&dup);

	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}
	if (!dup)
	{
		return (1);
	}
	return (0);
}
