import java.util.Scanner;

public class Blackjack {

	public static void main (String [] args) {

		Scanner input = new Scanner(System.in);

		System.out.println( "\nWelcome to Blackjack! You start with 100 chips." );
		int chips = 100;

		int play = 1;
		while (play == 1) {

		System.out.print( "\nPlease place your bet " );
		int bet = input.nextInt();

			while (bet > chips) {
			System.out.print( "\nYou have bet too many chips. Please try again " );
			bet = input.nextInt();
			}

		int PlayerTotal = 0;
		int DealerTotal = 0;
		int cards = 1;

		int deck[] = new int[52];
		String suits[] = {"Spades", "Hearts", "Diamonds", "Clubs"};
		String ranks[] = {"Ace", "2", "3", "4", "5", "6", "7", "8",
		"9", "10", "Jack", "Queen", "King"};

		for (int a = 0; a < deck.length; a++)
			deck[a] = a;

		for (int a = 0; a < deck.length; a++) {
			int index = (int) (Math.random() * deck.length);
			int temp = deck[a];
			deck[a] = deck[index];
			deck[index] = temp;
		}

		System.out.println( "\nHere are your two cards: " );
		PlayerTotal = GiveCard(suits, ranks, deck, PlayerTotal, 2);
		System.out.println( "\nYour total is " + PlayerTotal );

		deck = NextCards(deck, 2);

		System.out.println( "\nHere is the dealer's card: " );
		DealerTotal = GiveCard(suits, ranks, deck, DealerTotal, 1);
		System.out.println( "\nHis total is " + DealerTotal );

		int PlayerDeals = 0;
		deck = NextCards(deck, 1);
		cards = ScoreCheck(PlayerTotal, cards, PlayerDeals);
		PlayerDeals ++;

		while (cards == 1) {
		System.out.print( "\nEnter 1 for another card or 0 for none " );
		cards = input.nextInt();
		PlayerTotal = GiveCard(suits, ranks, deck, PlayerTotal, cards);
		cards = ScoreCheck(PlayerTotal, cards, PlayerDeals);
		System.out.println( "\nYour new total is " + PlayerTotal );
		deck = NextCards(deck, 1);
		PlayerDeals ++;
		}

		System.out.println();

		int DealerDeals = 0;
		while (DealerTotal < 17 && cards == 0) {
		DealerTotal = GiveCard(suits, ranks, deck, DealerTotal, 1);
		System.out.println( "\nHis new total is " + DealerTotal );
		cards = ScoreCheck(DealerTotal, cards, DealerDeals);
		deck = NextCards(deck, 1);
		DealerDeals ++;
		}

		if (PlayerTotal > 21) {
			System.out.println( "\nYou lost " + bet + " chips" );
			chips -= bet;
			System.out.println( "\nYour new chip total is " + chips );
		}

		else if(DealerTotal > 21) {
			System.out.println( "\nYou won " + bet + " chips!" );
			chips += bet;
			System.out.println( "\nYour new chip total is " + chips );
		}

		else if (PlayerTotal == 21 && PlayerDeals == 1) {
			bet = (int) Math.floor( bet * 1.5 );
			System.out.println( "\nYou won " + bet + " chips!" );
			chips += bet;
			System.out.println( "\nYour new chip total is " + chips );
		}

		else if (PlayerTotal == 21 && PlayerDeals > 1) {
			System.out.println( "\nYou won " + bet + " chips!" );
			chips += bet;
			System.out.println( "\nYour new chip total is " + chips );
		}

		else if (PlayerTotal > DealerTotal) {
			System.out.println( "\nYou won " + bet + " chips!" );
			chips += bet;
			System.out.println( "\nYour new chip total is " + chips );
		}

		else if (PlayerTotal == DealerTotal) {
			System.out.println( "\nNobody won any chips" );
			System.out.println( "Your chip total is " + chips );
		}

		else if (DealerTotal > PlayerTotal) {
			System.out.println( "\nYou lost " + bet + " chips" );
			chips -= bet;
			System.out.println( "\nYour new chip total is " + chips );
		}

		if (chips != 0) {
			System.out.print( "\nWould you like to play another hand? 1 - yes, 0 - no " );
			play = input.nextInt();
		}


		if (chips == 0) {
			System.out.println( "\nYou have ran out of chips" );
			play = 0;
		}

		} //end while

		System.out.println( "\nThank you for playing Blackjack!" );
		System.out.println( "\nWinnings:" );

		if (chips - 100 == 0) 
			System.out.println( "You broke even" );

		else if (chips - 100 > 0)
			System.out.println( "You won " + (chips - 100) + " chips!" );

		else if (chips - 100 < 0)
			System.out.println( "You lost " + ((chips - 100) * -1) + " chips" );

	} //End of main


	public static int GiveCard(String suits[], String ranks[], int deck[],int PlayerTotal, int moves) {

		for (int a = 0; a < moves; a++) {
			String suit = suits[deck[a] / 13];
			String rank = ranks[deck[a] % 13];
			System.out.println("Card number " + deck[a] + ": " +
			rank + " of " + suit);

			switch (rank) {

				case "Ace": PlayerTotal += 11;
				break;

				case "Jack": PlayerTotal += 10;
				break;

				case "Queen": PlayerTotal += 10;
				break;

				case "King": PlayerTotal += 10;
				break;

				default: PlayerTotal += Integer.parseInt(rank);
				break;
			}

		}

		return PlayerTotal;
	}

	public static int ScoreCheck(int total, int cards, int deals) {

		if (total == 21 && deals == 0) {
			System.out.println( "\nBlackjack!" );
			cards = 2;
			return cards;
		}

		else if (total == 21) {
			cards = 0;
			return cards;
		}

		else if (total > 21) {
			System.out.println( "\nBusted!" );
			cards = 2;
			return cards;
		}

		else
			return cards;
	}


	public static int[] NextCards(int deck[], int moves) {

		while (moves > 0) {

		int temp = deck[0];
		int temp2 = deck[1];

		for (int a = 1; a < deck.length; a++)
			deck[a - 1] = deck[a];

		deck[deck.length - 2] = temp;
		deck[deck.length - 1] = temp2;

		moves --;
		}

		return deck;
	}
}
