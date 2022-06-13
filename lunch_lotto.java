import java.util.*;

public class lunch_lotto {
   
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ArrayList<Student> students = new ArrayList<Student>();
        int i = 1;
        while (i == 1) {
            System.out.print("\nEnter your student ID: ");
            int id = input.nextInt();
            System.out.print("Enter your lunch period: ");
            int per = input.nextInt();
            students.add(new Student(id,per));
            System.out.print("Do you want to add another student? (Yes -> 1, No -> 0): ");
            i = input.nextInt();
        }
        assign(students);
        // input.close();
    }
   
    public static void assign(ArrayList<Student> s) {
        for (int p = 1; p <= maxPer(s); p++) {
            ArrayList<Student> thisPer = new ArrayList<Student>();
            for (int i = 0; i < s.size(); i++) {
                if (s.get(i).getPer() == p) {
                    thisPer.add(s.get(i));
                }
            }
            for (int i = 0; i < thisPer.size(); i++) {
                thisPer.get(i).setGrpNum((i / 4) + 1);
            }
            if (thisPer.size() > 0) {
                System.out.println("Lunch Period " + p + ":");
                for (int i = 1; i <= thisPer.get(thisPer.size()-1).getGrpNum(); i++) {
                    System.out.println("  Group " + i + ":");
                    for (int j = 0; j < thisPer.size(); j++) {
                        if (thisPer.get(j).getGrpNum() == i) {
                            System.out.println("    " + thisPer.get(j).getID());
                        }
                    }
                }
            }
        }
    }
   
    public static int maxPer(ArrayList<Student> s) {
        int maxP = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s.get(i).getPer() > maxP)
                maxP = s.get(i).getPer();
        }
        return maxP;
    }
}

class Student {
   
    private int id;
    private int period;
    private int grpNum;
   
    public Student () {
        id = 1;
        period = 1;
    }
   
    public Student (int theID, int thePer) {
        id = theID;
        period = thePer;
    }
   
    public int getID () {
        return id;
    }
   
    public void setID (int theID) {
        id = theID;
    }
   
    public int getPer () {
        return period;
    }
   
    public void setPer (int thePer) {
        period = thePer;
    }
   
    public int getGrpNum () {
        return grpNum;
    }
   
    public void setGrpNum (int theGrpNum) {
        grpNum = theGrpNum;
    }
   
    public String toString () {
        return ("Your ID: " + getID() + "\nYour Lunch Period: " + getPer());
    }
}