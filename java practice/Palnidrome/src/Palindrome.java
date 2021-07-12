import java.util.*;

class Palindrome
{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        
        System.out.println("Input a word or sentence");
        String str=sc.nextLine();
        
        System.out.println("Input a word or sentence"+str+"is Palindrome ? "+isPalindrome(str));

    }
  static boolean isPalindrome(String text)
  {
    String reverse=reverse(text);
    if(text.equals(reverse)){
        return true;
    }
        return false;   
  }  

  static String reverse(String input){
      if(input==null||input.isEmpty())
      return input;
      return input.charAt(input.length()-1) + reverse(input.substring(0, input.length()-1));
  }

}

