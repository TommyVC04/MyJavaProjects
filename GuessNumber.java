import java.util.Scanner;

public class GuessNumber
{
	public static void main( String [] args )
	{
		int restart = 1;
		while (restart == 1) {
		
		Scanner input = new Scanner(System.in);

		System.out.println();
		System.out.println( "Think of a number between 1 and 50\n" +
		"I will try to guess what it is by asking you some questions" );

		String set1 = 
		"1  3  5  7  9\n" +
		"11 13 15 17 19\n" +
		"21 23 25 27 29\n" +
		"31 33 35 37 39\n" +
		"41 43 45 47 49";

		String set2 = 
		"2  3  6  7  10\n" +
		"11 14 15 18 19\n" +
		"22 23 26 27 30\n" +
		"31 34 38 42 43\n" +
		"46 47 50";

		String set3 = 
		"4  5  6  7  12\n" +
		"13 14 15 20 21\n" +
		"22 23 28 29 30\n" +
		"31 36 37 38 44\n" +
		"45 46 47";

		String set4 = 
		"8  9  10 11 12\n" +
		"13 14 15 24 25\n" +
		"26 27 28 29 30\n" +
		"31 40 41 42 43\n" +
		"44 45 46 47";

		String set5 = 
		"16 17 18 19 20\n" +
		"21 22 23 24 25\n" +
		"26 27 28 29 30\n" +
		"31 48 49 50";

		String set6 =
		"32 33 34 35 36\n" +
		"37 38 39 40 41\n" +
		"42 43 44 45 46\n" +
		"47 48 49 50";

		int day = 0;

		System.out.println();
		System.out.println( "Is your number in Set 1?" );
		System.out.print( set1 );
		System.out.println( "\nEnter 0 for No and 1 for Yes" );
		int answer = input.nextInt();

		if (answer != 0 && answer != 1) {
		System.out.println( "\nPlease enter 0 for No or 1 for Yes" );
		answer = input.nextInt(); }

		if (answer == 1)
		day += 1;

		System.out.println();
		System.out.println( "Is your number in Set 2?" );
		System.out.print( set2 );
		System.out.println( "\nEnter 0 for No and 1 for Yes" );
		answer = input.nextInt();

		if (answer != 0 && answer != 1) {
		System.out.println( "\nPlease enter 0 for No or 1 for Yes" );
		answer = input.nextInt(); }

		if (answer == 1)
		day += 2;

		System.out.println();
		System.out.println( "Is your number in Set 3?" );
		System.out.print( set3 );
		System.out.println( "\nEnter 0 for No and 1 for Yes" );
		answer = input.nextInt();

		if (answer != 0 && answer != 1) {
		System.out.println( "\nPlease enter 0 for No or 1 for Yes" );
		answer = input.nextInt(); }

		if (answer == 1)
		day += 4;

		System.out.println();
		System.out.println( "Is your number in Set 4?" );
		System.out.print( set4 );
		System.out.println( "\nEnter 0 for No and 1 for Yes" );
		answer = input.nextInt();

		if (answer != 0 && answer != 1) {
		System.out.println( "\nPlease enter 0 for No or 1 for Yes" );
		answer = input.nextInt(); }

		if (answer == 1)
		day += 8;

		System.out.println();
		System.out.println( "Is your number in Set 5?" );
		System.out.print( set5 );
		System.out.println( "\nEnter 0 for No and 1 for Yes" );
		answer = input.nextInt();

		if (answer != 0 && answer != 1) {
		System.out.println( "\nPlease enter 0 for No or 1 for Yes" );
		answer = input.nextInt(); }

		if (answer == 1)
		day += 16;

		System.out.println();
		System.out.println( "Is your number in Set 6?" );
		System.out.print( set6 );
		System.out.println( "\nEnter 0 for No and 1 for Yes" );
		answer = input.nextInt();

		if (answer != 0 && answer != 1) {
		System.out.println( "\nPlease enter 0 for No or 1 for Yes" );
		answer = input.nextInt(); }

		if (answer == 1)
		day += 32;

		if (day > 50 || day < 1) {
		System.out.println();
		System.out.println( "Your number is not in the list" ); }

		else {
		System.out.println();
		System.out.println( "Your number is " + day + "!" ); }

		System.out.println();
		System.out.println( "Would you like to try again?\n" +
		"0 for No and 1 for Yes" );
		restart = input.nextInt();

		if (restart != 1 && restart != 0) {
		System.out.println();
		System.out.println( "Please enter 1 to try again or 0 to stop" );
		restart = input.nextInt();
		}
		
		}
		
		System.out.println();
		System.out.println( "Thank you, I hope you had your mind BLOWN!!" );
	}
}