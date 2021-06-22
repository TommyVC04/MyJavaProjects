import java.util.Scanner;

public class EpidemicCreator
{
	public static void main( String [] args )
	{
		Scanner input = new Scanner(System.in);
		int restart = 1;

		//while restart start
		while (restart == 1) {

		System.out.println( "\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" );
		System.out.println( "\nWelcome to the Epidemic Creator!" );
		System.out.println( "\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" );
		System.out.println( "\nYou will be able to change the " +
		"parameters of your epidemic to simulate a population!" );
		System.out.println( "The variables are:" );
		System.out.println( "\nPopulation Size = Amount of people " +
		"in simulation \nInfection Rate = What percent of the " +
		"population contracts the disease \nFatality Rate = What " +
		"percent of infected people die from the disease \nCure " +
		"Rate = What percent of infected people recover from the " +
		"disease \nPopulation annual growth rate is 0.6%" );

		System.out.println( "\nWhat is the Population Size?" );
		double popSize = input.nextDouble();

		System.out.println( "\nEnter following amounts as percentages" +
		" from 1-100 (Ex. If you want 10%, enter 10)" );
		System.out.println( "\nWhat is the Infection Rate?" );
		double infRate = input.nextDouble();

		System.out.println( "\nWhat is the Fatality Rate?" );
		double fatRate = input.nextDouble();

		System.out.println( "\nWhat is the Cure Rate?" );
		double curRate = input.nextDouble();

		

		int continueSim = 1;
		int generation = 1;
		double popSizeR = popSize;
		double infRateR = 0;
		double fatRateR = 0;
		double curRateR = 0;
		double newOff = 0;

		System.out.println( "\nYear 0" );
		System.out.println( "\nGross Population Growth = " + newOff);
		System.out.println( "# of people Infected = " + infRateR );
		System.out.println( "# of people Killed = " + fatRateR );
		System.out.println( "# of people Cured = " + curRateR );		
		System.out.println( "Population Size (Accounting for " +
		"annnual growth rate) = " + popSizeR );

		System.out.println( "\nWould you like to simulate another " +
		"year?  Enter 1 for yes or 0 for no" );
		continueSim = input.nextInt();
		

		if (continueSim != 1 && continueSim != 0) {
		System.out.println( "\nPlease enter 1 to simulate another " +
		"year or 0 to not" );
		continueSim = input.nextInt();
		}

		//while continue start
		while (continueSim == 1) {
		
		System.out.println( "\nYear " + generation );

		newOff = Math.floor(popSizeR * 0.006);
		infRateR = Math.ceil((popSizeR - curRateR) * ( infRate / 100 ));
		fatRateR = Math.ceil(infRateR * ( fatRate / 100 ));
		curRateR = Math.ceil(infRateR * (curRate / 100));
		popSizeR = Math.ceil(popSizeR + newOff - fatRateR);


		if (fatRateR <= 0) {
		System.out.println( "\nYour population has deminished" );
		continueSim = 0;
		}

		if (fatRateR > 0) {
		System.out.println( "\nGross Population Growth = " + newOff);
		System.out.println( "# of people Infected = " + infRateR );
		System.out.println( "# of people Killed = " + fatRateR );
		System.out.println( "# of people Cured = " + curRateR );		
		System.out.println( "Population Size (Accounting for " +
		"annnual growth rate) = " + popSizeR );

		


		//End of generation
		System.out.println( "\nWould you like to simulate another " +
		"year?  Enter 1 for yes or 0 for no" );
		continueSim = input.nextInt();
		}


		generation += 1;

		if (continueSim != 1 && continueSim != 0) {
		System.out.println( "\nPlease enter 1 to simulate another " +
		"year or 0 to not" );
		continueSim = input.nextInt();
		}

		}
		//while continue end


		System.out.println( "\nWould you like to make a new epidemic" +
		"?  Enter 1 for yes or 0 for no" );
		restart = input.nextInt();

		if (restart != 1 && restart != 0) {
		System.out.println( "\nPlease enter 1 to restart or 0 to quit" );
		restart = input.nextInt();
		}

		}
		//while restart end

		System.out.println( "\nThank you for using the Epidemic " +
		"Creator!" );

	}
}