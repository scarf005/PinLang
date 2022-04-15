#include "pin.h"
#include <stdio.h>
int	main(void)
{
	while (1)
		printf("I'm getting used to this !");
	system("leaks -zsh");
	return (0);
}
