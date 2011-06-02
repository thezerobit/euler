#include "stdio.h"

int triangle(int num)
{
  return (num * (num + 1)) / 2;
}

int countdivs(int num)
{
  int count = 2;
  int i;
  int top = num;
  int half = num / 2;
  int other; 
  for(i = 2; i <= half && i < top ; i++)
  {
    if((num % i) == 0)
    {
      other = num / i;
      if (i < other)
      {
        count += 2;
        top = other;
      }
      else if (i == other)
      {
        count ++;
        return count;
      }
    }
  }
  return count;
}

int main()
{
  int i, greatest, tri, count,gt;
  greatest = 0;
  gt = 0;
  i = 0;
  while(1)
  {
    i++;
    /* printf("%d -> %d\n", i, triangle(i)); */
    tri = triangle(i);
    count = countdivs(tri);
    if (count > greatest)
    {
      if(count > 500) {
	 printf("answer : %d\n", tri);
         printf("%d -> %d -> %d\n", i, tri, count);
         return 0;
      }
      greatest = count;
      gt = tri;
      printf("%d -> %d -> %d\n", i, tri, count);
    } 
  }
  printf("hello\n");
  return 0;
}
