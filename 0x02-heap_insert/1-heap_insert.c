#include"binary_trees.h"
/**
 * heap_insert - function that inserts a value into a Max Binary Heap
 * @root: is a double pointer to the root node of the Heap
 * @value: is the value store in the node to be inserted
 *
 * Return: a pointer to the inserted node, or NULL on failure
 **/
heap_t *heap_insert(heap_t **root, int value)
{
	heap_t *new_node = NULL;

	new_node = malloc(sizeof(*new_node));

	if (!new_node)
		return (NULL);

	new_node->n = value;
	new_node->left = NULL;
	new_node->right = NULL;
	new_node->parent = *root;

	return (new_node);
}
