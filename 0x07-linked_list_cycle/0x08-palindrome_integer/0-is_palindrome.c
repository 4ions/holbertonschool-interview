#include "palindrome.h"

/**
* is_palindrome - Checks if number is a palindrome
*
* @n: Number being checked
*
* Return: 1 if palindrome, 0 if not
*/
int is_palindrome(unsigned long n)
{
	unsigned long temp = n;
	unsigned long reverse = 0;
	unsigned long remainder;

	while (n != 0)
	{
		remainder = n % 10;

		/* Each loop the remainder is added to reverse to build up n in reverse */
		reverse = reverse * 10 + remainder;

		/* Stops the while loop when n is 0 */
		n /= 10;
	}

	if (temp == reverse)
	{
		return (1);
	}
	return (0);
}
