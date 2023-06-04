class UptopianTree 
{
  public static int utopianTree(int n ) 
  {
    int h = 1;

    for (int i = 1; i < (n + 1); i++) {
      if ((i == 1) || (i % 2 == 0)) {
        h = h + 1;
      } else {
        h = h * 2;
      }
    }

    return h;
  }
}
