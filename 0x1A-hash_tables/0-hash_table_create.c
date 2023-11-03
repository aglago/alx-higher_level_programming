#include "hash_tables.h"

/**
 * hash_table_create - creates a hash table
 * A hash_table_t is an array of pointers
 * to a hash items
 *
 * @size: the size of the array
 *
 * Return: a pointer to a table
 */
hash_table_t *hash_table_create(int size)
{
	unsigned long int i = 0;
	/* create table */
	hash_table_t *table = malloc(sizeof(hash_table_t));

	/* set table attributes */
	table->size = size;
	table->array = calloc(table->size, sizeof(hash_node_t*));

	/* set all elements to NULL */
	for (; i < table->size; i++)
		table->array[i] = NULL;

	/* return table created */
	return (table);
}
