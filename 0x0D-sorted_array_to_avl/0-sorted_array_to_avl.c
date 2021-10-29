#include "binary_trees.h"
/**
* binary_tree_node - creates a binary tree node
* @parent: parent node
* @value: value for the new node
* Return: the new node
*/
binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)
{
	binary_tree_t *new;

	new = malloc(sizeof(binary_tree_t));
	if (new == NULL)
		return (NULL);
	new->left = NULL;
	new->right = NULL;
	new->n = value;
	new->parent = parent;
	return (new);
}
/**
* splice_array - builds an AVL tree from an array
* @array: array to be converted
* @start: start of array
* @end: end of array
* @parent: parent node
* Return: pointer to the root node
*/
avl_t *splice_array(int *array, size_t start, size_t end, avl_t *parent)
{
	avl_t *root;
	size_t mid;

	mid = (start + end) / 2;
	root = binary_tree_node(parent, array[mid]);
	if (root == NULL)
		return (NULL);
	if (start > end)
		return (NULL);
	if (mid != start)
		root->left = splice_array(array, start, mid - 1, root);
	if (mid != end)
		root->right = splice_array(array, mid + 1, end, root);
	return (root);
}
/**
* sorted_array_to_avl - builds an AVL tree from an array
* @array: array to be converted
* @size: number of elements in the arra
* Return: pointer to the root node
*/
avl_t *sorted_array_to_avl(int *array, size_t size)
{
	avl_t *root;

	if (array == NULL || size == 0)
		return (NULL);
	root = splice_array(array, 0, size - 1, NULL);
	return (root);
}
