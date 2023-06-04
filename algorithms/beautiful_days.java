public static int reverse(int a)
{
    int reverse = 0;
    while(a!=0)
    {
        reverse = reverse * 10;
        reverse = reverse + a%10;
        a = a/10;
    }
    return reverse;
}

public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int i = in.nextInt();
    int j = in.nextInt();
    int k = in.nextInt();

    int count = 0;
    for(int a = i;a<j+1;a++)
    {           
       int d= a-reverse(a);
       if(d%k==0)
           count++;
    }
    System.out.println(count);
}
