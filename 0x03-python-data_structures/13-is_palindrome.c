#include "lists.h"

/**
 * is_palindrome - is a linked list palindromic ?
 * @head: head of list passed into function
 * Return: 1 if palindromic and 0 if not
 *
 * AUTHOR - Ami Manye
 */
int is_palindrome(listint_t **head)
{
	int i = 0, rev_i = 0, check_i = 0, nodes_int[2048], rev_nodes_int[2048];
	listint_t *curr = NULL;

	if (*head == NULL)
		return (1);

	/* traverse list to insert each node value into array */
	curr = *head;
	while (curr)
	{
		nodes_int[i] = curr->n;
		/*printf("nodes_int[%d] = %d\n", i, nodes_int[i]);*/
		i++;
		curr = curr->next;
	}
	/*printf("Number of nodes are: %d\n", i);*/

	/* loop through array and put its values into rev array */
	/*printf("i at this point is: %d\n", i);*/
	i--;
	while (i >= 0)
	{
		/*printf("i inside the loop is: %d\n", i);*/
		rev_nodes_int[rev_i] = nodes_int[i];
		/*printf("rev_nodes_int[%d] = %d\n", rev_i, rev_nodes_int[rev_i]);*/
		if (rev_nodes_int[rev_i] != nodes_int[check_i])
		{
			/*printf("rev_nodes_int[%d]: %d != nodes_int[%d]: \n", rev_i, rev_nodes_int[rev_i], check_i, nodes_int[check_i]);*/
			return (0);
		}
		i--;
		rev_i++;
		check_i++;
	}
	return (1);
}
