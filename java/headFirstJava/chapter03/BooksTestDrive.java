package chapter03;

public class BooksTestDrive {
	public static void main(String[] args) {
		Books[] myBooks = new Books[3];
		int x = 0;
		for (int i = 0 ; i < myBooks.length ; i++) {
			myBooks[i] = new Books();
		}
		myBooks[0].title = "Book One";
		myBooks[1].title = "Book Two";
		myBooks[2].title = "Book Three";
		myBooks[0].author = "Auth ONE";
		myBooks[1].author = "Auth TWO";
		myBooks[2].author = "Auth THREE";
		
		
		while ( x<3) {
			System.out.print(myBooks[x].title);
			System.out.print(" by ");
			System.out.println(myBooks[x].author);
			x +=1;
		}
	}
}
