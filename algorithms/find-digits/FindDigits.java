class FindDigits {
	public static void main (String[] args) {
		int n = in.nextInt();
		int r = n;
		int count = 0;
		
		while(r > 0){
			if(r % 10 != 0 && n % (r % 10) == 0) count++;
			r = r / 10;
		}
		
		System.out.println(count);
	}
}
