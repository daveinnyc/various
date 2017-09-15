package grade;

/**
 *
 * @author dave
 */
public class ReportCard {
    String studentName;
    
    public char convertGrades(int result){
        char grade;    
        
        // Chapter uses the style:  result > 79 && result < 90 
        if(result > 89){
            grade = 'A';
        } else if(result > 79){
            grade = 'B';
        } else if(result > 75){
            grade = 'C';
        } else if(result > 69){
            grade = 'D';
        } else {
            grade = 'F';
        }
        
        return grade;
    }
        
    public String gradeComment(char grade){
        String commentText = new String();
        
        switch(grade){
            case 'A':
                commentText = "Great";
                break;
            case 'B':
                commentText = "OK";
                break;
            case 'C':
                commentText = "Meh";
                break;
            case 'D':
                commentText = "Not good";
                break;
            case 'F':
                commentText = "Doomed";
                break;
        }    
        return commentText;            
    }
}
