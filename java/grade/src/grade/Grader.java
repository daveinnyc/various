package grade;

/**
 *
 * @author dave
 */
public class Grader {
    public static void main(String[] args) {
         ReportCard report = new ReportCard();
         String comment;
         
         for(int i = 63; i < 100; i = i + 5){
             char grade = report.convertGrades(i);
             comment = report.gradeComment(grade);
             System.out.println(i + " is " + grade + " " + comment);
             
         }
    }
    
}
