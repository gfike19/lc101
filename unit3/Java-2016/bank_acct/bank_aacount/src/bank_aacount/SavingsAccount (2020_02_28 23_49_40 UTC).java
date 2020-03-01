package bank_aacount;

public class SavingsAccount {
private Integer balance; //will always add up to the sum of its parts
private double interest_rate;

public SavingsAccount(Integer balance, double interest_rate){
	this.balance = balance;
	this.interest_rate = interest_rate;
}

public Integer getBalance() {
	return this.balance;
}

public double getInterest_rate(){
	return this.interest_rate;
}

public Integer add(Integer amount){
	this.balance =+ amount;
	return this.balance;
} 

public Integer remove(Integer amount){
	this.balance =- amount;
	return this.balance;
}

public Integer accrue (){
	Integer interest = (int) (this.balance * this.interest_rate); //can cast from int to Integer
	this.balance =+ interest;
	return this.balance;
}

public String toString (){
	return "balance: " + this.balance + " " + "interest: " + this.interest_rate;
}

public static void main(String[]args){
	
	SavingsAccount test_acct = new SavingsAccount(100, .25);
	System.out.println("current bal is: " + test_acct.getBalance());
	test_acct.add(test_acct.getBalance()*2);
	System.out.println("current bal is: " + test_acct.getBalance());
	test_acct.remove(test_acct.getBalance()* 5);
	System.out.println("current bal is: " + test_acct.getBalance());
	test_acct.accrue(); //toString reps something as a string
	System.out.println("current bal is: " + test_acct.getBalance());
}
}

